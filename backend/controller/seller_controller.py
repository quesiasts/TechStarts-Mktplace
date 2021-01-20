from backend.controller.base_controller import BaseController
from backend.dao_bd.seller_dao import SellerDao


class SellerController(BaseController):
    def __init__(self) -> None:
        self.__dao = SellerDao()
        super().__init__(self.__dao, "Seller")
