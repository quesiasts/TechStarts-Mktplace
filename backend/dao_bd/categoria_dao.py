from .connection import Connection

from .base_dao import BaseDao
from backend.models.categoria import Category

class CategoryDao(BaseDao):
    def create(self, categoria: Category)-> list:
        query = f""" INSERT INTO CATEGORY
                            (NAME, DESCRIPTION)
                            VALUES
                            ('{categoria.name}',
                            '{categoria.description}'); """
        super().execute(query)
            

    def read_by_id(self, id: int) -> Category:        
        query = f"SELECT name, description, id FROM category WHERE ID={id}"
        result = super().read(query) [0]
        categoria = Category(result[0], result[1], result[2])
        return categoria


    def read_all(self) -> list:
        query = f"SELECT name, description, id FROM category"
        result_list = super().read(query)
        categorias = []              
        for result in result_list:
            categoria = Category(result[0], result[1], result[2])        
            categorias.append(categoria)        
        return categorias


    def update(self, categoria: Category) -> None:        
        query = f"""UPDATE category
                                SET 
                                name = '{categoria.name}',
                                description = '{categoria.description}'
                                WHERE id = '{categoria.id}'"""
        super().execute(query)
        

    def delete(self, id: int) -> None:        
        query = f"DELETE FROM category WHERE id = '{id}'"
        super().execute(query)

    
