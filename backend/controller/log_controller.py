import sys
sys.path.append('.')
#from backend.dao_txt.log import listar_log
from backend.dao_bd.log_dao import *


def listar_logs() -> list:
    return listar_log_bd()