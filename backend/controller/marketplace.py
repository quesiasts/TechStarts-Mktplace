import sys
sys.path.append('.')
from backend.dao_txt.marketplace import criar_marketplace, listar_marketplace
from backend.dao_bd.log import criar_log
from backend.dao_bd.marketplace import *


def criar_marketplaces(nome:str, descricao:str) -> None:
    criar_marketplace_bd(nome, descricao)
    criar_log(f'Marketplace {nome} criada!')

def listar_marketplaces() -> list:
    criar_log(f'Marketplace listado!')
    return listar_marketplace_bd()