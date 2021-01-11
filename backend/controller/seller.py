import sys
sys.path.append('.')
#from backend.dao_txt.seller import criar_seller, listar_seller
#from backend.dao_txt.log import criar_log
from backend.dao_bd.seller import *
from backend.dao_bd.log import *


def criar_sellers(nome:str, email:str, telefone:str) -> None:
    criar_seller_bd(nome, email, telefone)
    criar_log_bd(f'Seller {nome} criada!')


def listar_sellers() -> list:
    criar_log_bd(f'Seller listado!')
    return listar_seller_bd()