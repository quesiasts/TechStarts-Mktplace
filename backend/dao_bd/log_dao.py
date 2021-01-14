from .connection import Connection
from backend.models.log import Log



def criar_log_bd(log: Log) -> None:
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO log (description) VALUES ('{log.description}');")
        connection.commit()
    
    
def listar_log_bd() -> list:
    logs = []    
    with Connection() as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, date, hour, description FROM log")
        linhas = cursor.fetchall()        
        for linha in linhas:
            datetime = linha[1].strftime("%d/%m/%Y") + ' - ' + str(linha[2])
            log = Log(linha[3],  datetime, linha[0])         
            logs.append(log)        
    return logs