from backend.dao_bd.base_dao import BaseDao
from backend.models.produto import Product


class ProductDao(BaseDao):
    def __init__(self):
        super().__init__(Product)
