from pathlib import Path


_path_categorias = 'dados/categorias.txt'

def criar_categoria(nome:str, descricao:str) -> None:
    with open(_path_categorias, 'a') as categorias_file:
        categorias_file.write(f'{nome};{descricao}\n')
        

def listar_categoria() -> list:
    categorias = []
    file = Path(_path_categorias)
    if file.is_file():
        with open(_path_categorias, 'r') as categorias_file:
            for i in categorias_file:
                i = i.strip().split(';')
                i = {'nome': i[0],
                    'descricao': i[1]
                    }
                categorias.append(i)
        return categorias
    else:
        return []
