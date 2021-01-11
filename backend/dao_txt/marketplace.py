from pathlib import Path


_path_marketplaces = 'dados/marketplaces.txt'


def criar_marketplace(nome:str, descricao:str) -> None:
    marketplaces_file = open(_path_marketplaces, 'a')
    marketplaces_file.write(f'{nome};{descricao}\n')
    marketplaces_file.close()

def listar_marketplace() -> list:
    marketplaces = []
    file = Path(_path_marketplaces)
    if file.is_file():
        marketplaces_file = open(_path_marketplaces, 'r')
        for i in marketplaces_file:
            i = i.strip().split(';')
            i = {'nome': i[0],
                'descricao': i[1]
                }
            marketplaces.append(i)
        marketplaces_file.close()
        return marketplaces
    else:
        return []
