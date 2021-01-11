import sys
sys.path.append('.')
from backend.dao_txt.categoria import criar_categoria, listar_categoria
from backend.dao_txt.log import criar_log


def criar_categorias(nome:str, descricao:str) -> None:
    criar_categoria(nome, descricao)
    criar_log(f'Categoria {nome} criada!')

def listar_categorias() -> list:
    criar_log(f'Categoria listada!')
    return listar_categoria()
    