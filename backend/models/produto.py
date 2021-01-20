from sqlalchemy import Column, String, Numeric
from backend.models.base_model import BaseModel


class Product(BaseModel):
    __tablename__ = 'product'

    name = Column(String(length=200))
    description = Column(String(length=200))
    price = Column(Numeric)

    def __init__(self, name: str, description: str, price: float) -> None:
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Name: {self.name}, Description: {self.description}, Price: {self.price}"
  
    