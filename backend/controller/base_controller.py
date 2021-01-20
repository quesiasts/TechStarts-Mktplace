from sqlalchemy.orm.exc import NoResultFound

from backend.controller.log_controller import LogController
from backend.dao_bd.base_dao import BaseDao
from backend.models.base_model import BaseModel

log = LogController()


class BaseController:
    def __init__(self, dao: BaseDao, domain_name: str):
        self.__dao = dao
        self.__domain_name = domain_name

    def create(self, model: BaseModel) -> None:
        self.__dao.save(model)
        log.create(f"{self.__domain_name} criado(a)", "cadastrando")

    def read_all(self) -> list:
        result = self.__dao.read_all()
        log.create(f"{self.__domain_name} listados", "listando")
        return result

    def read_by_id(self, id: int) -> BaseModel:
        try:
            result = self.__dao.read_by_id(id)
        except NoResultFound:
            raise Exception('Item not Found.')
        log.create(f"{self.__domain_name} lido", "lendo")
        return result

    def update(self, model: BaseModel) -> None:
        self.read_by_id(model.id)
        self.__dao.save(model)
        log.create(f"{self.__domain_name} atualizado(a)", "atualizando")

    def delete(self, id: int):
        result = self.read_by_id(id)
        self.__dao.delete(result)
        log.create(f"{self.__domain_name} deletado(a)", "deletando")
