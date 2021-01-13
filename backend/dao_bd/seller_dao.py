from .conexao import *
from backend.models.seller import Seller



def criar_seller_bd(seller: Seller) -> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO sellers (name, email, phone) VALUES ('{seller.name}', '{seller.email}', '{seller.phone}');")
        connection.commit()
        
    
def listar_seller_bd() -> list:
    sellers = []    
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sellers")
        linhas = cursor.fetchall()        
        for linha in linhas:
            seller = Seller(linha[0], linha[1], linha[2], linha[3])
            sellers.append(seller)        
    return sellers