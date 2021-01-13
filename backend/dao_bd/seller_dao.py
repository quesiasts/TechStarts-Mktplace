import sys
sys.path.append('.')

from backend.conexao_bd.conexao import *
from backend.models.seller import Seller
from .conexao import *


def criar_seller_bd(seller: Seller) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO sellers (name, email, phone) VALUES ('{seller.name}', '{seller.email}', '{seller.phone}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_seller_bd() -> list:    
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sellers")
    linhas = cursor.fetchall()
    sellers = []
    for linha in linhas:
        seller = Seller(linha[0], linha[1], linha[2], linha[3])
        sellers.append(seller)    
    cursor.close()
    conn.close()
    return sellers