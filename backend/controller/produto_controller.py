import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.produto_dao import ProductDao

class ProductController(BaseController):
    def __init__(self):
        self.__dao = ProductDao()
        domain_name = "Produto"
        super().__init__(self.__dao, domain_name)

