LOAD = 0
RUN = 1
MONGODB = 0
MONGODB_CLUSTER = 1
MSSQL = 2

REQS = None
REQS2 = None
mssql_connection = None
mongodb_client = None

HOSTIP = "127.0.0.1"
BASEPATH = "/home/atz2nd/Desktop/editycsb/YCSB/"
RESULTPATH = "./ycsb-results/"
MONGO_URL = "mongodb://%s:27017" % HOSTIP
MONGO_CLUSTER_URL = None
SQL_EXPORT_DB = 'ycsb'
RECORDS_COL = 'usertable'
MSSQLUSER = 'sa'
MSSQLPWD = 'MSSQL-pwd'

DBS = [MSSQL, MONGODB]
WORKLOADS = ['a', 'b', 'c', 'd', 'e', 'f']
RC_OP_COUPLES = [(10, 5), (20, 10)]
# THREADS_NO = [1] + list(range(2, 33, 2))
THREADS_NO = [1, 2, 4]
RUNS_NO = 3
LOAD_TC = 4