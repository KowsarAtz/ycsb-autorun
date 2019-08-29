LOAD = 0
RUN = 1
MONGODB = 0
MONGODB_CLUSTER = 1
MSSQL = 2
MARIADB = 3
ELASTIC5 = 4
DIFFERENT_LOADS = 1

REQS = None
REQS2 = None
mssql_connection = None
mongodb_client = None
mysql_connection = None

HOSTIP = "172.16.13.26"
# HOSTIP = "localhost"
BASEPATH = "/mnt/hdd2/nosql-prj/YCSB/YCSB/"
# BASEPATH = "/home/atz2nd/Desktop/YCSB/"
RESULTPATH = "./ycsb-results/"
MONGO_URL = "mongodb://%s:27023" % HOSTIP
MONGO_CLUSTER_URL = "mongodb://%s:27021" % HOSTIP
SQL_EXPORT_DB = 'ycsb'
RECORDS_COL = 'usertable'
MSSQLUSER = 'sa'
MSSQLPWD = 'MSSql-pwd'
# MSSQLPWD = 'MSSQL-pwd'

# DBS = [MSSQL, MARIADB, MONGODB, MONGODB, ELASTIC5]
DBS = [ELASTIC5]
WORKLOADS = ['A', 'B']
RC_OP_COUPLES = [(1000, 1000),(10000,10000),(100000,100000)]
# RC_OP_COUPLES = [(20,20),(30,30)]
THREADS_NO = [1,2,4,8]
RUNS_NO = 5
LOAD_TC = 1

CHARTRESULTPATH = "./chart-results/"
CHARTSREFRENCE = "./ycsb-results/"
CHARTSWLSREFRENCE = WORKLOADS
CHARTCOUNTSREFRENCE = RC_OP_COUPLES
CHARTTHREADCOUNTS = THREADS_NO
CHARTWIDTH = 1000
CHARTHEIGHT = 500
COMPARINGDBS_SET = [['mssql','mariadb', 'mongodb', 'elastic5']]
COMPARINGDBS_SET += [['mongodb', 'mongodb-async']]