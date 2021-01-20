from sqlalchemy.orm import sessionmaker

from backend.dao_bd.base_dao import BaseDao
from backend.models.categoria import Category

class CategoryDao(BaseDao):
    def __init__(self) -> None:
        super().__init__(Category) 

    


   