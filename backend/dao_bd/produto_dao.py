from .connection import Connection
from backend.models.produto import Produto


def criar_produto_bd(produto: Produto) -> None:
    with Connection() as connection:
        cursor = connection.cursor()    
        cursor.execute(f"INSERT INTO product (name, description, price) VALUES ('{produto.name}', '{produto.description}', {produto.price});")
        connection.commit()
        
    
    
def listar_produto_bd() -> list:
    products = []
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, name, description, price FROM product")
        linhas = cursor.fetchall()        
        for linha in linhas:
            product = Produto(linha[1], linha[2], linha[3], linha[0])       
            products.append(product)        
    return products
