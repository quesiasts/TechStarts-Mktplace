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


def update_categoria_bd(categoria: Categoria) -> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"UPDATE category SET name = '{categoria.name}', description = '{categoria.description}'  WHERE id = '{categoria.id}'")
        connection.commit()
    

def delete_categoria_bd(id: int) -> None:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"DELETE FROM category WHERE id = '{id}'")
        connection.commit()

def get_category_by_id(id: int) -> Categoria:
    with psycopg2.connect(dados_conexao()) as connection:
        cursor = connection.cursor()
        cursor.execute(f"SELECT name, description, id FROM category WHERE ID={id}")
        linha = cursor.fetchone()
        categoria = Categoria(linha[0], linha[1], linha[2])
        return categoria
