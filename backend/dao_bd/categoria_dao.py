
from .conexao import *

def criar_categoria_bd(nome:str, descricao:str) -> None:
    with psycopg2.connect(dados_conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute(f"INSERT INTO category (name, description) VALUES ('{nome}', '{descricao}');")
        conn.commit()
    
def listar_categoria_bd() -> list:
    categorias = []
    with psycopg2.connect(dados_conexao()) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM category")
        cat = cursor.fetchall()
        for c in cat:
            c = {'nome': c[1],
                'descricao': c[2]
                }
            categorias.append(c)
    return categorias