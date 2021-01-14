import sys
sys.path.append('.')

from backend.dao_bd.log_dao import *
from backend.dao_bd.produto_dao import *
from backend.models.produto import Produto



def criar_produtos(produto:Produto) -> None:
    criar_produto_bd(produto)
    log = Log(f'Produto {produto.name} criado!' )
    criar_log_bd(log)

def listar_produtos() -> list:
    produtos = listar_produto_bd()
    log = Log(f'Produto listado!' )
    criar_log_bd(log)
    return produtos

