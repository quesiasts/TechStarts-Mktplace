import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.categoria_dao import CategoryDao

class CategoryController(BaseController):
    def __init__(self):
        self.__dao = CategoryDao()
        super().__init__(self.__dao)
