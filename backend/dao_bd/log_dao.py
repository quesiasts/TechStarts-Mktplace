from backend.models.log import Log
from .base_dao import BaseDao


class LogDao(BaseDao):
    def create(self, log: Log)-> list:
        query = f""" INSERT INTO log
                            (description, date, hour, action)
                            VALUES
                            ('{log.description}',
                            '{log.date}',
                            '{log.hour}',
                            '{log.action}'); """
        super().execute(query)
            

    def read_log(self) -> list:
        query = f"SELECT description, date, hour, action FROM log;"
        result_list = super().read(query)
        logs = []
        for log in result_list:
            log = Log(log[0], log[1],log[2], log[3])
            logs.append(log)
        return logs
