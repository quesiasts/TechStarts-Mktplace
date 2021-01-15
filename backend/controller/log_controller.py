import sys
sys.path.append('.')

from backend.dao_bd.log_dao import *
from datetime import datetime
from backend.models.log import Log

class LogController():
    def __init__(self):
        self.__dao = LogDao()
    
    def create(self, description, action) -> None:
        date = datetime.now().strftime('%Y-%m-%d')
        hour = datetime.now().strftime('%H:%M:%S')
        log = Log(description, date, hour, action)
        self.__dao.create(log)
        
    def read_all(self) -> list:
        return self.__dao.read_log()
        
