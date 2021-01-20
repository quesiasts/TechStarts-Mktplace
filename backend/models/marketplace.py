import sqlalchemy as sql
from backend.models.base_model import BaseModel


class Marketplace(BaseModel): 
    __tablename__ = 'marketplace'

    name = sql.Column( sql.String(length=200), nullable=False )
    description = sql.Column( sql.String(length=200), nullable=True )

    def __init__(self, name:str, description:str) -> None:
        self.name = name
        self.description = description
