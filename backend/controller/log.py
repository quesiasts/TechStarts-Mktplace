import sys
sys.path.append('.')
from backend.dao_txt.log import listar_log


def listar_logs() -> list:
    return listar_log()