LOAD = 0
RUN = 1
MONGODB = 0
MONGODB_CLUSTER = 1
MSSQL = 2
MARIADB = 3
ELASTIC5 = 4
SYNC_ASYNC = 0

REQS = None
REQS2 = None
mssql_connection = None
mongodb_client = None
mysql_connection = None

HOSTIP = "172.16.13.26"
BASEPATH = "/mnt/hdd2/nosql-prj/YCSB/YCSB/"
RESULTPATH = "./ycsb-results/"
MONGO_URL = "mongodb://%s:27023" % HOSTIP
MONGO_CLUSTER_URL = "mongodb://%s:27021" % HOSTIP
SQL_EXPORT_DB = 'ycsb'
RECORDS_COL = 'usertable'
MSSQLUSER = 'sa'
MSSQLPWD = 'MSSql-pwd'

DBS = [ELASTIC5,MONGODB]
# WORKLOADS = ['a', 'b', 'c', 'd', 'e', 'f']
WORKLOADS = ['c']
# RC_OP_COUPLES = [(1000, 1000)]
RC_OP_COUPLES = [(1000, 1000)]
# THREADS_NO = [1, 2, 4, 8, 12, 16]
# THREADS_NO = [3]
THREADS_NO = [1]
RUNS_NO = 1
LOAD_TC = 8

CHARTRESULTPATH = "./chart-results/"
CHARTSREFRENCE = "./chartref/"
CHARTSWLSREFRENCE = ['c']
CHARTCOUNTSREFRENCE = [(1000,1000), (10000,10000)]
CHARTTHREADCOUNTS = [1]
CHARTWIDTH = 1000
CHARTHEIGHT = 500
# COMPARINGDBS_SET = [['mssql', 'mariadb', 'mongodb', 'mongodb-async', 'mongodbcluster1', 'mongodbcluster1-async']]
COMPARINGDBS_SET = [['mongodb', 'elastic5']]