from .connection import Connection


class BaseDao:
    def execute(self, query:str) -> None:
        with Connection() as connection:
            cursor.execute(query)
            connection.commit()   
            
        
    def list_all(self, query:str) -> tuple:
        with Connection() as connection:
            cursor.connection.cursor()
            cursor.execute(query)
            result = cursor.fechall()
        return result
        


    