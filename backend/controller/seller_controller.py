from backend.controller.base_controller import BaseController
from backend.dao_bd.seller_dao import SellerDao


class SellerController(BaseController):
    def __init__(self):
        self.__dao = SellerDao()
        self.domain_name = "Seller"
        super().__init__(self.__dao, self.domain_name)
