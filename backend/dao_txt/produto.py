from pathlib import Path


_path_produtos = 'dados/produtos.txt'


def criar_produto(nome:str, descricao:str, preco:float) -> None:
    produtos_file = open(_path_produtos, 'a')
    produtos_file.write(f'{nome};{descricao};{preco}\n')
    produtos_file.close()

def listar_produto() -> list:
    produtos = []
    file = Path(_path_produtos)
    if file.is_file():
        produtos_file = open(_path_produtos, 'r')
        for produto in produtos_file:
            aux = produto.strip().split(';') 
            p = {'nome': aux[0],
                'descricao': aux[1],
                'preco': aux[2]
                }
            produtos.append(p)
        produtos_file.close()
        return produtos
    else:
        return []
    