import sys
sys.path.append('.')

from backend.dao_bd.seller_dao import *
from backend.dao_bd.log_dao import *
from backend.models.seller import Seller


def criar_sellers(seller: Seller) -> None:
    criar_seller_bd(seller)
    log = Log(None, None, f'Seller {seller.name} cadastrado!' )
    criar_log_bd(log)


def listar_sellers() -> list:
    sellers = listar_seller_bd()
    log = Log(None, None, f'Seller listado!')
    criar_log_bd(log)
    return sellers