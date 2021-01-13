from .conexao import *
from backend.models.produto import Produto


def criar_produto_bd(produto: Produto) -> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()    
        cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{produto.name}', '{produto.description}', {produto.price});")
        connection.commit()
        
    
    
def listar_produto_bd() -> list:
    products = []
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM product")
        linhas = cursor.fetchall()        
        for linha in linhas:
            product = Produto(linha[0], linha[1], linha[2], linha[3])        
            products.append(product)        
    return products
