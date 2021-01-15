from .connection import Connection

from .base_dao import BaseDao
from backend.models.seller import Seller

class SellerDao(BaseDao):
    def create(self, seller: Seller)-> list:
        query = f""" INSERT INTO sellers
                            (NAME, PHONE, EMAIL)
                            VALUES
                            ('{seller.name}',
                            '{seller.phone}',
                            '{seller.email}'); """
        super().execute(query)
            

    def read_by_id(self, id: int) -> Seller:        
        query = f"SELECT name, email, phone, id FROM sellers WHERE ID={id}"
        result = super().read(query) [0]
        sellers = Seller(result[0], result[2], result[1], result[3])
        return sellers


    def read_all(self) -> list:
        query = f"SELECT name, email, phone, id FROM sellers"
        result_list = super().read(query)
        sellers = []              
        for result in result_list:
            seller = Seller(result[0], result[2], result[1], result[3])        
            sellers.append(seller)        
        return sellers


    def update(self, seller: Seller) -> None:        
        query = f"""UPDATE sellers
                                SET 
                                name = '{seller.name}',
                                email = '{seller.email}',
                                phone = '{seller.phone}'
                                WHERE id = {seller.id}"""
        super().execute(query)
        

    def delete(self, id: int) -> None:        
        query = f"DELETE FROM sellers WHERE id = '{id}'"
        super().execute(query)