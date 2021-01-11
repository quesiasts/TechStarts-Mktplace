import sys
sys.path.append('.')
from backend.dao_txt.produto import criar_produto, listar_produto
from backend.dao_txt.log import criar_log


def criar_produtos(nome:str, descricao:str, preco:float) -> None:
    criar_produto(nome, descricao, preco)
    criar_log(f'Produto {nome} criada!')

def listar_produtos() -> list:
    criar_log(f'Produto listado!')
    return listar_produto()