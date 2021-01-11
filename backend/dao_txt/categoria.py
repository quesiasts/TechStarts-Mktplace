from pathlib import Path


_path_categorias = 'dados/categorias.txt'

def criar_categoria(nome:str, descricao:str) -> None:
    categorias_file = open(_path_categorias, 'a')
    categorias_file.write(f'{nome};{descricao}\n')
    categorias_file.close()

def listar_categoria() -> list:
    categorias = []
    file = Path(_path_categorias)
    if file.is_file():
        categorias_file = open(_path_categorias, 'r')
        for i in categorias_file:
            i = i.strip().split(';')
            i = {'nome': i[0],
                'descricao': i[1]
                }
            categorias.append(i)
        categorias_file.close()
        return categorias
    else:
        return []
