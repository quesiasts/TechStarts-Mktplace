from backend.dao_bd.session import Session
from .base_dao import BaseDao
from backend.models.seller import Seller

class SellerDao(BaseDao):
    def __init__(self):
        super().__init__(Seller)

