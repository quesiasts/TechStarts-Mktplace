from pathlib import Path


_path_sellers = 'dados/sellers.txt'


def criar_seller(nome:str, email:str, telefone:str) -> None:
    seller_file = open(_path_sellers, 'a')
    seller_file.write(f'{nome};{email};{telefone}\n')
    seller_file.close()

def listar_seller() -> list:
    sellers = []
    file = Path(_path_sellers)
    if file.is_file():
        sellers_file = open(_path_sellers, 'r')
        for seller in sellers_file:
            aux = seller.strip().split(';')
            p = {'nome': aux[0],
                'email': aux[1],
                'telefone': aux[2]
                }
            sellers.append(p)
        sellers_file.close()
        return sellers
    else:
        return []
