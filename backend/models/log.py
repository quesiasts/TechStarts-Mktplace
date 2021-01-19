from sqlalchemy import Column, String, Date, func, Time

from backend.models.base_model import BaseModel


class Log(BaseModel):
    __tablename__ = 'log'
    description = Column(String(length=200), nullable=False)
    action = Column(String(length=200), nullable=False)
    date = Column(Date, server_default=func.current_date(), nullable=False)
    time = Column(Time, server_default=func.current_time(), nullable=False)

    def __init__(self, description: str, action: str, date: str = None, hour: str = None, id: str = None) -> None:
        self.id = id
        self.date = date
        self.hour = hour
        self.description = description
        self.action = action
