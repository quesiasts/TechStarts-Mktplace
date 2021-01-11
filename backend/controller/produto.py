import sys
sys.path.append('.')
from backend.dao_bd.log import *
from backend.dao_bd.produto import *


def criar_produtos(nome:str, descricao:str, preco:float) -> None:
    criar_produto_bd(nome, descricao, preco)
    criar_log_bd(f'Produto {nome} criada!')

def listar_produtos() -> list:
    criar_log_bd(f'Produto listado!')
    return listar_produto_bd()