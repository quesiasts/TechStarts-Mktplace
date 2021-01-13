import sys
sys.path.append('.')

from backend.conexao_bd.conexao import *
from backend.models.marketplace import Marketplace


def criar_marketplace_bd(marketplace: Marketplace) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplaces (marketplace_name, description) VALUES ('{marketplace.name}', '{marketplace.description}');")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def listar_marketplace_bd() -> list:
    marketplaces = []
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()

    cursor.execute("SELECT id, marketplace_name, description FROM marketplaces")
    linhas = cursor.fetchall()
    marketplaces = []
    for linha in linhas:
        marketplace = Marketplace(linha[0], linha[1], linha[2])        
        marketplaces.append(marketplace)
    cursor.close()
    conn.close()
    return marketplaces
