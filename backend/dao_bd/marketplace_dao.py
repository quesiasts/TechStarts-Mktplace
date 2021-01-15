from .connection import Connection

from .base_dao import BaseDao
from backend.models.marketplace import Marketplace

class MarketplaceDao(BaseDao):
    def create(self, marketplace: Marketplace)-> list:
        query = f""" INSERT INTO marketplaces
                            (NAME, DESCRIPTION)
                            VALUES
                            ('{marketplace.name}',
                            '{marketplace.description}'); """
        super().execute(query)
            

    def read_by_id(self, id: int) -> Marketplace:        
        query = f"SELECT name, description, id FROM marketplaces WHERE ID={id}"
        result = super().read(query) [0]
        marketplace = Marketplace(result[0], result[1], result[2])
        return marketplace


    def read_all(self) -> list:
        query = f"SELECT name, description, id FROM marketplaces"
        result_list = super().read(query)
        marketplaces = []              
        for result in result_list:
            marketplace = Marketplace(result[0], result[1], result[2])        
            marketplaces.append(marketplace)        
        return marketplaces


    def update(self, marketplace: Marketplace) -> None:        
        query = f"""UPDATE marketplaces
                                SET 
                                name = '{marketplace.name}',
                                description = '{marketplace.description}'
                                WHERE id = '{marketplace.id}'"""
        super().execute(query)
        

    def delete(self, id: int) -> None:        
        query = f"DELETE FROM marketplaces WHERE id = '{id}'"
        super().execute(query)
