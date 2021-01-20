import sqlalchemy
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    __tablename__ = 'seller'
    name = sqlalchemy.Column(sqlalchemy.String(length=200))
    phone = sqlalchemy.Column(sqlalchemy.String(length=200))
    email = sqlalchemy.Column(sqlalchemy.String(length=200))
        

    def __init__(self, name:str, phone:str, email:str, id:int=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.id = id