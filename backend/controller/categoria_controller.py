import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.categoria_dao import CategoryDao

class CategoryController(BaseController):
    def __init__(self, type_entity):
        self.__dao = CategoryDao()
        self.type_entity = type_entity
        super().__init__(self.__dao, self.type_entity)
