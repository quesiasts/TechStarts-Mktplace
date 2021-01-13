import sys
sys.path.append('.')
#from backend.dao_txt.log import listar_log
from backend.dao_bd.log import *
from backend.models.log import Log


def listar_logs() -> list:
    logs = listar_log_bd()
    return logs