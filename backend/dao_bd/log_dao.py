from sqlalchemy.orm.exc import NoResultFound

from backend.dao_bd.base_dao import BaseDao
from backend.dao_bd.session import Session
from backend.models.log import Log


class LogDao(BaseDao):
    def __init__(self):
        super().__init__(Log)

    def save(self, model: Log) -> None:
        try:
            self.read_by_id(model.id)
        except NoResultFound:
            raise Exception('You cannot modify a log!')

        with Session() as session:
            session.add(model)
            session.commit()
