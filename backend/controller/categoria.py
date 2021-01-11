import sys
sys.path.append('.')
#from backend.dao_txt.categoria import criar_categoria, listar_categoria
#from backend.dao_txt.log import criar_log
from backend.dao_bd.categoria import *
from backend.dao_bd.log import *


def criar_categorias(nome:str, descricao:str) -> None:
    criar_categoria_bd(nome, descricao)
    criar_log_bd(f'Categoria {nome} criada!')


def listar_categorias() -> list:
    criar_log_bd(f'Categoria listada!')
    return listar_categoria_bd()
    