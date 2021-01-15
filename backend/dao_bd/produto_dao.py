from .connection import Connection

from .base_dao import BaseDao
from backend.models.produto import Product

class ProductDao(BaseDao):
    def create(self, product: Product)-> list:
        query = f""" INSERT INTO product
                            (NAME, DESCRIPTION, PRICE)
                            VALUES
                            ('{product.name}',
                            '{product.description}',
                            '{product.price}'); """
        super().execute(query)
            

    def read_by_id(self, id: int) -> Product:        
        query = f"SELECT name, description, price, id FROM product WHERE ID={id}"
        result = super().read(query) [0]
        products = Product(result[0], result[1], result[2], result[3])
        return products


    def read_all(self) -> list:
        query = f"SELECT name, description, price, id FROM product"
        result_list = super().read(query)
        products = []              
        for result in result_list:
            product = Product(result[0], result[1], result[2], result[3])        
            products.append(product)        
        return products


    def update(self, product: Product) -> None:        
        query = f"""UPDATE product
                                SET 
                                name = '{product.name}',
                                description = '{product.description}',
                                price = '{product.price}'
                                WHERE id = '{product.id}'"""
        super().execute(query)
        

    def delete(self, id: int) -> None:        
        query = f"DELETE FROM product WHERE id = '{id}'"
        super().execute(query)
