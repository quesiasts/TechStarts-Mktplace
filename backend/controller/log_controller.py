import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.log_dao import *

class LogController(BaseController):
    def __init__(self):
        self.__dao = LogDao()
        super().__init__(self.__dao)
