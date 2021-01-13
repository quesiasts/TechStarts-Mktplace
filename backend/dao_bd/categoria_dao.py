from .conexao import *
from backend.models.categoria import Categoria



def criar_categoria_bd(categoria: Categoria)-> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO category (name, description) VALUES ('{categoria.name}', '{categoria.description}');")
        connection.commit()
        
    
def listar_categoria_bd() -> list:
    categorias = []   
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT name, description, id FROM category")
        linhas = cursor.fetchall()        
        for linha in linhas:
            categoria = Categoria(linha[0], linha[1], linha[2])        
            categorias.append(categoria)        
    return categorias



