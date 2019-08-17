LOAD = 0
RUN = 1
MONGODB = 0
MONGODB_CLUSTER = 1
MSSQL = 2

REQS = None
REQS2 = None
mssql_connection = None
mongodb_client = None

HOSTIP = "172.16.13.26"
BASEPATH = "/mnt/hdd2/nosql-prj/YCSB/YCSB/"
RESULTPATH = "./ycsb-results/"
MONGO_URL = "mongodb://%s:27023" % HOSTIP
MONGO_CLUSTER_URL = "mongodb://%s:27021" % HOSTIP
SQL_EXPORT_DB = 'ycsb'
RECORDS_COL = 'usertable'
MSSQLUSER = 'sa'
MSSQLPWD = 'MSSql-pwd'

DBS = [MONGODB_CLUSTER]
WORKLOADS = ['a', 'b', 'c', 'd', 'e', 'f']
RC_OP_COUPLES = [(1000, 1000)]
# THREADS_NO = [1] + list(range(2, 33, 2))
THREADS_NO = [1, 2, 4, 8, 12, 16]
RUNS_NO = 3
LOAD_TC = 8