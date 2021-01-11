import sys
sys.path.append('.')
from backend.dao_txt.seller import criar_seller, listar_seller
from backend.dao_txt.log import criar_log


def criar_sellers(nome:str, email:str, telefone:str) -> None:
    criar_seller(nome, email, telefone)
    criar_log(f'Seller {nome} criada!')

def listar_sellers() -> list:
    criar_log(f'Seller listado!')
    return listar_seller()