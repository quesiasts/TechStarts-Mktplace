from .conexao import *
from backend.models.marketplace import Marketplace


def criar_marketplace_bd(marketplace: Marketplace) -> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO marketplaces (marketplace_name, description) VALUES ('{marketplace.name}', '{marketplace.description}');")
        connection.commit()
        
    
    
def listar_marketplace_bd() -> list:
    marketplaces = []
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, marketplace_name, description FROM marketplaces")
        linhas = cursor.fetchall()        
        for linha in linhas:
            marketplace = Marketplace(linha[0], linha[1], linha[2])        
            marketplaces.append(marketplace)   
    return marketplaces
