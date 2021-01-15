from backend.models.log import Log

from .base_dao import BaseDao
from .connection import Connection


class LogDao(BaseDao):

    def create(self, log: Log) -> None:
        query = f"INSERT INTO log (description) VALUES ('{log.description}')"
        super().execute(query)        
        
    def read_all(self) -> list:
        query = f"SELECT id, date, hour, description FROM log"
        linhas = super().read(query)
        logs = []
        for linha in linhas:
            datetime = linha[1].strftime("%d/%m/%Y") + ' - ' + str(linha[2])
            log = Log(linha[3],  datetime, linha[0])         
            logs.append(log)        
        return logs
