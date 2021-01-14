from .connection import Connection
from backend.models.seller import Seller



def criar_seller_bd(seller: Seller) -> None:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO sellers (name, email, phone) VALUES ('{seller.name}', '{seller.email}', '{seller.phone}');")
        connection.commit()
        
    
def listar_seller_bd() -> list:
    sellers = []    
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM sellers")
        linhas = cursor.fetchall()        
        for linha in linhas:
            seller = Seller(linha[1], linha[3], linha[2], linha[0])
            sellers.append(seller)        
    return sellers