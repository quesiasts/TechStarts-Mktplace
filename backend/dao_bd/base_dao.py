from typing import ClassVar

from backend.dao_bd.session import Session
from backend.models.base_model import BaseModel


class BaseDao:
    def __init__(self, model_type: ClassVar) -> None:
        self.__model_type = model_type

    def save(self, model: BaseModel) -> None:
        with Session() as session:
            session.add(model)
            session.commit()

    def read_all(self) -> list:
        with Session() as session:
            return session.query(self.__model_type).all()

    def read_by_id(self, id: int) -> BaseModel:
        with Session() as session:
            return session.query(self.__model_type).filter_by(id=id).one()

    def delete(self, model: BaseModel) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()
