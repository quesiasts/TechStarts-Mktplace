from sqlalchemy.orm.exc import NoResultFound

from backend.dao_bd.log_dao import LogDao
from backend.exceptions.log_exceptions import LogNotFoundException
from backend.models.log import Log


class LogController:
    def __init__(self):
        self.__dao = LogDao()

    def create(self, description: str, action: str) -> None:
        log = Log(description, action)
        self.__dao.save(log)

    def read_all(self) -> list:
        return self.__dao.read_all()

    def read_by_id(self, id: int) -> Log:
        try:
            result = self.__dao.read_by_id(id)
        except NoResultFound:
            raise LogNotFoundException
        return result

    def delete(self, id: int) -> None:
        log = self.read_by_id(id)
        self.__dao.delete(log)
