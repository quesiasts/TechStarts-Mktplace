import sys
sys.path.append('.')
from backend.dao_txt.marketplace import criar_marketplace, listar_marketplace
from backend.dao_bd.log import *
from backend.dao_bd.marketplace import *
from backend.models.marketplace import Marketplace


def criar_marketplaces(marketplace: Marketplace) -> None:
    criar_marketplace_bd(marketplace)
    criar_log_bd(f'Marketplace {marketplace.name} criado!')

def listar_marketplaces() -> list:
    marketplaces = listar_marketplace_bd()
    criar_log_bd(f'Marketplace listado!')
    return marketplaces