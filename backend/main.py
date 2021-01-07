from pathlib import Path
from datetime import datetime

path_marketplaces = 'dados/marketplaces.txt'
path_produtos = 'dados/produtos.txt'
path_sellers = 'dados/sellers.txt'
path_log = 'dados/log.txt'


def get_marketplaces():
    marketplaces = []
    file = Path(path_marketplaces)
    if file.is_file():
        marketplaces_file = open(path_marketplaces, 'r')
    else:
        marketplaces_file = open(path_marketplaces, 'x')
    for i in marketplaces_file:
        i = i.strip()
        j = i.split(';')
        i = {'nome': j[0],
             'descricao': j[1]
             }
        marketplaces.append(i)
    marketplaces_file.close()
    set_log('get_marketplaces - buscar marketplaces')
    return marketplaces


def set_marketplaces(nome, descricao):
    if nome == '':
        return 'Nome não pode ser vazio'
    for marketplace in get_marketplaces():
        if marketplace['nome'] == nome:
            return 'Nome do Marketplace já existe!'
    file = Path(path_marketplaces)
    if file.is_file():
        marketplaces_file = open(path_marketplaces, 'a')
    else:
        marketplaces_file = open(path_marketplaces, 'x')
    marketplaces_file.write(f'{nome};{descricao}\n')
    marketplaces_file.close()
    set_log('set_marketplaces - adicionar marketplaces')
    return 'Marketplace cadastrado com sucesso!!!'


def get_produtos():
    produtos = []
    file = Path(path_produtos)
    if file.is_file():
        produtos_file = open(path_produtos, 'r')
    else:
        produtos_file = open(path_produtos, 'x')
    for produto in produtos_file:
        aux = produto.strip()  # cadeira;descrição;20,00
        # aux[0] -> cadeira; aux[1] -> descrição; aux[2] -> 20,00
        aux = aux.split(';')
        p = {'nome': aux[0],
             'descricao': aux[1],
             'preco': aux[2]
             }
        produtos.append(p)
    produtos_file.close()
    set_log('get_produtos - buscar produtos')
    return produtos


def set_produtos(nome, descricao, preco):
    if nome == '':
        return 'Nome não pode ser vazio'
    for produto in get_produtos():
        if produto['nome'] == nome:
            return 'Nome do Produto já existe!'
    file = Path(path_produtos)
    if file.is_file():
        produtos_file = open(path_produtos, 'a')
    else:
        produtos_file = open(path_produtos, 'x')
    produtos_file.write(f'{nome};{descricao};{preco}\n')
    produtos_file.close()
    set_log('set_produtos - adicionar produtos')
    return 'Produto cadastrado com sucesso!!!'


def get_seller():
    sellers = []
    file = Path(path_sellers)
    if file.is_file:
        sellers_file = open(path_sellers, 'r')
    else:
        sellers_file = open(path_sellers, 'x')
    for seller in sellers_file:
        aux = seller.strip()
        aux = aux.split(';')
        p = {'primeiro_nome': aux[0],
             'segundo_nome': aux[1],
             'email': aux[2],
             'telefone': aux[3]
             }
        sellers.append(p)
    sellers_file.close()
    set_log('get_sellers - buscar sellers')
    return sellers


def set_seller(primeiro_nome, segundo_nome, email, telefone):
    if primeiro_nome == '' or segundo_nome == '' or email == '' or telefone == '':
        return 'Nenhum campo pode estar vazio!'
    for seller in get_seller():
        if seller['email'] == email:
            print(seller['email'])
            return 'O e-mail informado já está em uso!'
    file = Path(path_sellers)
    if file.is_file():
        seller_file = open(path_sellers, 'a')
    else:
        seller_file = open(path_sellers, 'x')
    seller_file.write(f'{primeiro_nome};{segundo_nome};{email};{telefone}\n')
    seller_file.close()
    set_log('set_seller - adicionar novo seller')
    return 'Seller cadastrado com sucesso!!!'


def set_log(log):
    file = Path(path_log)
    if file.is_file():
        log_file = open(path_log, 'a')
    else:
        log_file = open(path_log, 'x')
    dataHora = datetime.now()
    dataHora = dataHora.strftime("%d /%m /%y access the %H:%M h/m.")
    log_file.write(f'{dataHora} - {log}\n')
    log_file.close()
