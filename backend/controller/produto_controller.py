from backend.controller.base_controller import BaseController
from backend.dao_bd.produto_dao import ProductDao


class ProductController(BaseController):
    def __init__(self) -> None:
        self.__dao = ProductDao()
        domain_name = "Produto"
        super().__init__(self.__dao, domain_name)

