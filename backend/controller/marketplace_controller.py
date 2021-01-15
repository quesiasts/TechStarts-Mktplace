import sys
sys.path.append('.')

from .base_controller import BaseController
from backend.dao_bd.marketplace_dao import MarketplaceDao

class MarketplaceController(BaseController):
    def __init__(self):
        self.__dao = MarketplaceDao()
        super().__init__(self.__dao)


