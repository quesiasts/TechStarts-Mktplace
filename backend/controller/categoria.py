import sys
sys.path.append('.')
#from backend.dao_txt.categoria import criar_categoria, listar_categoria
#from backend.dao_txt.log import criar_log
from backend.dao_bd.categoria import *
from backend.dao_bd.log import *
from backend.models.categoria import Categoria


def criar_categorias(categoria: Categoria) -> None:
    criar_categoria_bd(categoria)
    criar_log_bd(f'Categoria {categoria.name} criada!')


def listar_categorias() -> list:
    categorias = listar_categoria_bd() 
    criar_log_bd(f'Categoria listada!')
    return categorias
    