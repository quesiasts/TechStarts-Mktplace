import sys
sys.path.append('.')
from backend.dao_txt.marketplace import criar_marketplace, listar_marketplace
from backend.dao_bd.log import *
from backend.dao_bd.marketplace import *
from backend.models.marketplace import Marketplace


def criar_marketplaces(marketplace: Marketplace) -> None:
    criar_marketplace_bd(marketplace)
    log = Log(None, None, f'Marketplace {marketplace.name} criado!' )
    criar_log_bd(log)

def listar_marketplaces() -> list:
    marketplaces = listar_marketplace_bd()
    log = Log(None, None, f'Marketplace listado!')
    criar_log_bd(log)
    return marketplaces


