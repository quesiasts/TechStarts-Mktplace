import sqlalchemy
from backend.models.base_model import BaseModel

class Seller(BaseModel):
    def _init_(self, name:str, phone:str, email:str, id:int=None):
        self.name = sqlalchemy.Column(sqlalchemy.String(length=200))
        self.phone = sqlalchemy.Column(sqlalchemy.String(length=200))
        self.email = sqlalchemy.Column(sqlalchemy.String(length=200))
        

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def email(self):
        return self.__email
        
    @id.setter
    def id(self, id):
        self.__id = id

    @name.setter
    def name(self, name):
        self.__name = name

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @email.setter
    def email(self, email):
        self.__email = email
    
    