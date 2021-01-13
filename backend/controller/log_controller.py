import sys
sys.path.append('.')

from backend.dao_bd.log_dao import *
from backend.models.log import Log


def listar_logs() -> list:
    logs = listar_log_bd()
    return logs