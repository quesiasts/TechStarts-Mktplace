from .conexao import *

def criar_seller_bd(nome:str, email:str, telefone:str) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO sellers (name, email, phone) VALUES ('{nome}', '{email}', '{telefone}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_seller_bd() -> list:
    sellers = []
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sellers")
    seller = cursor.fetchall()
    for s in seller:
        s = {'nome': s[1],
            'email': s[2],
            'telefone': s[3]
            }
        sellers.append(s)
    cursor.close()
    conn.close()
    return sellers