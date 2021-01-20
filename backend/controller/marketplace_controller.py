from backend.controller.base_controller import BaseController
from backend.dao_bd.marketplace_dao import MarketplaceDao


class MarketplaceController(BaseController):
    def __init__(self, type_entity):
        self.__dao = MarketplaceDao()
        self.type_entity = type_entity
        super().__init__(self.__dao, self.type_entity)


