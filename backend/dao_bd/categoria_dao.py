from .conexao import *
from backend.models.categoria import Categoria



def criar_categoria_bd(categoria: Categoria)-> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO category (name, description) VALUES ('{categoria.name}', '{categoria.description}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_categoria_bd() -> list:    
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()

    cursor.execute("SELECT name, description, id FROM category")
    linhas = cursor.fetchall()
    categorias = []
    for linha in linhas:
        categoria = Categoria(linha[0], linha[1], linha[2])        
        categorias.append(categoria)
    cursor.close()
    conn.close()
    return categorias



