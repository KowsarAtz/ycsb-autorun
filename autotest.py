import pymongo
import pymssql
import os

LOAD = 0
RUN = 1
MONGODB = 0
MONGODB_CLUSTER = 1
MSSQL = 2

HOSTIP = "127.0.0.1"
BASEPATH = "/home/atz2nd/Desktop/editycsb/YCSB/"
RESULTPATH = "./ycsb-results/"
MONGO_URL = "mongodb://%s:27017" % HOSTIP
MONGO_CLUSTER_URL = None
SQL_EXPORT_DB = 'ycsb'
RECORDS_COL = 'usertable'

DBS = [MSSQL, MONGODB]
WORKLOADS = ['a']
RC_OP_COUPLES = [(150, 100)]
# THREADS_NO = [1] + list(range(2, 33, 2))
THREADS_NO = [1, 2, 4, 8]
RUNS_NO = 5
LOAD_TC = 8

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
        if dbtype == MONGODB:
            cmd += " mongodb -s -p mongodb.url=" + MONGO_URL
        else:
            cmd += " mongodb -s -p mongodb.url=" + MONGO_CLUSTER_URL
    elif dbtype == MSSQL:
        dbname = "mssql"
        cmd += " mssql -s -P " + BASEPATH + "mssql/db.properties"
    cmd += " -P " + BASEPATH + "workloads/workload" + workload + " -p recordcount=" + str(recordcount) + " -threads " + str(threadcount)
    
    if cmdtype == RUN:
        cmd += " -p operationcount=" + str(operationcount)
    resultpath = RESULTPATH + dbname + "/" + workload + "/" + "rc" + str(recordcount) + "-"
    
    if cmdtype == LOAD:
        resultpath  += "op0/" 
    elif cmdtype == RUN:
        resultpath += "op" + str(operationcount) + "/"

    resultpath += "tc" + str(threadcount) + "/"
    cmd += " > " + resultpath + "run" + str(runnumber) + ".txt"
    os.system("mkdir -p "+resultpath)
    os.system(cmd)
    return


mssql_connection = None  
mongodb_client = None

def clear_database(dbtype):
    if dbtype == MONGODB or dbtype == MONGODB_CLUSTER:
        mydb = mongodb_client[SQL_EXPORT_DB]
        mycol = mydb[RECORDS_COL]
        mycol.delete_many({})
    elif dbtype == MSSQL:
        cursor = mssql_connection.cursor()
        cursor.execute("DELETE FROM [%s].[dbo].[%s]" % (SQL_EXPORT_DB, RECORDS_COL))
        mssql_connection.commit()


for db in DBS:
    if db == MSSQL:
        mssql_connection = pymssql.connect(server=HOSTIP, user='sa', password='MSSQL-pwd', database=SQL_EXPORT_DB)
    elif db == MONGODB:
        mongodb_client = pymongo.MongoClient(MONGO_URL)
    elif db == MONGODB_CLUSTER:
        mongodb_client = pymongo.MongoClient(MONGO_CLUSTER_URL)
    for wl in WORKLOADS:
        for rc_op in RC_OP_COUPLES:
            rc_count = rc_op[0]
            op_count = rc_op[1]
            clear_database(db)
            run_wlcmd(db, wl, rc_count, None, LOAD_TC, 0)
            for thrd in THREADS_NO:
                for run in range(1, RUNS_NO+1):
                    run_wlcmd(db, wl, rc_count, op_count, thrd, run)