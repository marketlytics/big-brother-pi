import os
class Config(object):
    BASE_ADDR     = "http://big-brother.herokuapp.com/api/records"
    NODE_ADDR     = BASE_ADDR + "/all"
    LOG_ADDR      = BASE_ADDR + "/getlog"
    COMPANY_ID    = os.environ["COMPANY_ID"]
    MAX_MSG_LEN   = ""