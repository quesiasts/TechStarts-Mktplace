import sys
sys.path.append('.')
from backend.dao_bd.categoria_dao import *
from backend.dao_bd.log_dao import *
from backend.models.categoria import Categoria

# CRUD

def criar_categorias(categoria: Categoria) -> None:
    criar_categoria_bd(categoria)
    log = Log(None, None, f'Categoria {categoria.name} criada!' )
    criar_log_bd(log)

def listar_categorias() -> list:
    categorias = listar_categoria_bd()
    log = Log(None, None, f'Categoria listada!')
    criar_log_bd(log)
    return categorias

    criar_log_bd(f'Categoria listada!')
    return listar_categoria_bd()

def get_by_id(id:int):
    pass

def update(category):
    pass

def delete(id:int):
    pass

    