from .connection import Connection
from backend.models.marketplace import Marketplace


def criar_marketplace_bd(marketplace: Marketplace) -> None:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO marketplaces (marketplace_name, description) VALUES ('{marketplace.name}', '{marketplace.description}');")
        connection.commit()
        
    
    
def listar_marketplace_bd() -> list:
    marketplaces = []
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, marketplace_name, description FROM marketplaces")
        linhas = cursor.fetchall()        
        for linha in linhas:
            marketplace = Marketplace(linha[1], linha[2], linha[0])        
            marketplaces.append(marketplace)   
    return marketplaces
