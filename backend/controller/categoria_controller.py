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

def edit_category(id:int):
    return get_category_by_id(id)

def update_categoria(categoria: Categoria) -> None:
    update_categoria_bd(categoria)
    log = Log(None, None, f'Categoria atualizada!')
    criar_log_bd(log)

def delete_categoria(id:int):
    delete_categoria_bd(id)





    