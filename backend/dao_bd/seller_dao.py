from .connection import Connection

from .base_dao import BaseDao
from backend.models.seller import Seller

class SellerDao(BaseDao):
    super().__init__(Seller)