import pymongo
import pymssql
import MySQLdb
import os
import re
from definereqs import definereqs
from props import *


def run_wlcmd(dbtype, workload, recordcount, operationcount, threadcount, runnumber):
    cmd = BASEPATH
    cmdtype = None
    if operationcount == None:
        cmdtype = LOAD
    else:
        cmdtype = RUN

    if cmdtype == LOAD:
        cmd += "bin/ycsb.sh load"
    elif cmdtype == RUN:
        cmd += "bin/ycsb.sh run"

    dbname = None
    if dbtype == MONGODB or dbtype == MONGODB_CLUSTER:
        dbname = "mongodb"
        driver_type = None
        if SYNC_ASYNC == 0:
            driver_type = "mongodb"
        else:
            driver_type = "mongodb-async"
        if dbtype == MONGODB:
            cmd += " "+driver_type+" -s -p mongodb.url=" + MONGO_URL
        else:
            cmd += " "+driver_type+" -s -p mongodb.url=" + MONGO_CLUSTER_URL
    elif dbtype == MSSQL:
        dbname = "mssql"
        cmd += " mssql -s -P " + BASEPATH + "mssql/db.properties"
    elif dbtype == MARIADB:
        dbname = "mariadb"
        cmd += " jdbc -s -P " + BASEPATH + "jdbc/db.properties"
    elif dbtype == ELASTIC5:
        dbname = "elastic5"
        cmd += " elasticsearch5-rest"

    cmd += " -P " + BASEPATH + "workloads/workload" + workload + \
        " -p recordcount=" + str(recordcount) 
    
    if dbtype !=ELASTIC5:
        cmd += " -threads " + str(threadcount)

    if cmdtype == RUN:
        cmd += " -p operationcount=" + str(operationcount)
    resultpath = RESULTPATH + dbname + "/" + \
        workload + "/" + "rc" + str(recordcount) + "-"

    if cmdtype == LOAD:
        resultpath += "op0/"
    elif cmdtype == RUN:
        resultpath += "op" + str(operationcount) + "/"

    resultpath += "tc" + str(threadcount) + "/"
    cmd += " > " + resultpath + "run" + str(runnumber) + ".txt"
    os.system("mkdir -p "+resultpath)
    os.system(cmd)
    return


def calmeans(dbtype, workload, recordcount, operationcount, threadcount):
    dbname = None
    if dbtype == MONGODB or dbtype == MONGODB_CLUSTER:
        dbname = "mongodb"
    elif dbtype == MSSQL:
        dbname = "mssql"
    elif dbtype == MARIADB:
        dbname = "mariadb"
    elif dbtype == ELASTIC5:
        dbname = "elastic5"
    resultpath = RESULTPATH + dbname + "/" + \
        workload + "/" + "rc" + str(recordcount) + "-"
    resultpath += "op" + str(operationcount) + "/"
    resultpath += "tc" + str(threadcount) + "/"

    f = open(resultpath+"/"+"means.txt", "w")
    for rq in REQS:
        mean = 0
        total = 0
        for rn in range(1, RUNS_NO+1):
            filename = resultpath+'run'+str(rn)+".txt"
            gp = re.search(r".*"+rq+".*\), (.*)",
                           open(filename, "r").read())
            if gp == None:
                continue
            gp = gp.group(1)
            num = float(gp)
            mean = mean * total / (total + 1) + num / (total + 1)
            total += 1
        f.write("%s %s\n" % (REQS2[REQS.index(rq)], str(round(mean, 1))))
    f.close()
    return


def clear_database(dbtype):
    if dbtype == MONGODB or dbtype == MONGODB_CLUSTER:
        mydb = mongodb_client[SQL_EXPORT_DB]
        mycol = mydb[RECORDS_COL]
        mycol.delete_many({})
    elif dbtype == MSSQL:
        cursor = mssql_connection.cursor()
        cursor.execute("DELETE FROM [%s].[dbo].[%s]" %
                       (SQL_EXPORT_DB, RECORDS_COL))
        mssql_connection.commit()
    elif dbtype == MARIADB:
        cursor = mysql_connection.cursor()
        cursor.execute("DELETE FROM " + RECORDS_COL)
        mysql_connection.commit()
    elif dbtype == ELASTIC5:
        os.system('curl -XDELETE "http://%s:9200/es.ycsb/"' % HOSTIP)
    return


def remove_extras(dbtype, rc_count):
    pass


for db in DBS:
    if db == MSSQL:
        mssql_connection = pymssql.connect(
            server=HOSTIP, user=MSSQLUSER, password=MSSQLPWD, database=SQL_EXPORT_DB)
    elif db == MONGODB:
        mongodb_client = pymongo.MongoClient(MONGO_URL)
    elif db == MONGODB_CLUSTER:
        mongodb_client = pymongo.MongoClient(MONGO_CLUSTER_URL)
    elif db == MARIADB:
        mysql_connection = MySQLdb.connect(host='localhost', user="root", passwd="password", db=SQL_EXPORT_DB)
    for wl in WORKLOADS:
        REQS = definereqs(wl)[0]
        REQS2 = definereqs(wl)[1]
        for rc_op in RC_OP_COUPLES:
            rc_count = rc_op[0]
            op_count = rc_op[1]
            clear_database(db)
            run_wlcmd(db, wl, rc_count, None, LOAD_TC, 0)
            for thrd in THREADS_NO:
                for run in range(1, RUNS_NO+1):
                    run_wlcmd(db, wl, rc_count, op_count, thrd, run)
                    if wl == 'd' or wl == 'e' or wl == 'D':
                        clear_database(db)
                        run_wlcmd(db, wl, rc_count, None, LOAD_TC, 0)
                calmeans(db, wl, rc_count, op_count, thrd)
