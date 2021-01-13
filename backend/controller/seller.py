import sys
sys.path.append('.')
#from backend.dao_txt.seller import criar_seller, listar_seller
#from backend.dao_txt.log import criar_log
from backend.dao_bd.seller import *
from backend.dao_bd.log import *
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