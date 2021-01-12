import sys
sys.path.append('.')

from backend.conexao_bd.conexao import *
from backend.models.produto import Produto


def criar_produto_bd(produto: Produto) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()    
    cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{produto.name}', '{produto.description}', {produto.price});")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def listar_produto_bd() -> list:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    linhas = cursor.fetchall()
    products = []
    for linha in linhas:
        product = Produto(linha[0], linha[1], linha[2], linha[3])        
        products.append(product)
    cursor.close()
    conn.close()
    return products
