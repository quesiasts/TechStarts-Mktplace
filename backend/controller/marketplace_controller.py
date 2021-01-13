import sys
sys.path.append('.')
from backend.dao_txt.marketplace_dao_txt import criar_marketplace, listar_marketplace
from backend.dao_bd.log_dao import *
from backend.dao_bd.marketplace_dao import *


def criar_marketplaces(nome:str, descricao:str) -> None:
    criar_marketplace_bd(nome, descricao)
    criar_log_bd(f'Marketplace {nome} criada!')

def listar_marketplaces() -> list:
    criar_log_bd(f'Marketplace listado!')
    return listar_marketplace_bd()