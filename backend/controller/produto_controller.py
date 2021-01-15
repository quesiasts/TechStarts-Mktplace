import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.produto_dao import ProductDao

class ProductController(BaseController):
    def __init__(self, type_entity):
        self.__dao = ProductDao()
        self.type_entity = type_entity
        super().__init__(self.__dao, self.type_entity)

