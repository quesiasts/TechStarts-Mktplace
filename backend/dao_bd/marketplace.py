import sys
sys.path.append('.')

from backend.conexao_bd.conexao import *


def criar_marketplace_bd(nome:str, descricao:str) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplaces (marketplace_name, description) VALUES ('{nome}', '{descricao}');")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def listar_marketplace_bd() -> list:
    marketplaces = []
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM marketplaces")
    mkt = cursor.fetchall()
    for i in mkt:
        i = {'nome': i[1],
            'descricao': i[2]
            }
        marketplaces.append(i)
    cursor.close()
    conn.close()
    return marketplaces
