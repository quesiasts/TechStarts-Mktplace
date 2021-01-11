import sys
sys.path.append('.')

from backend.conexao_bd.conexao import *

def criar_categoria_bd(nome:str, descricao:str) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO category (name, description) VALUES ('{nome}', '{descricao}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_categoria_bd() -> list:
    categorias = []
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM category")
    cat = cursor.fetchall()
    for c in cat:
        c = {'nome': c[1],
            'descricao': c[2]
            }
        categorias.append(c)
    cursor.close()
    conn.close()
    return categorias