
from backend.conexao_bd.conexao import *
from backend.models.log import Log
from .conexao import *


def criar_log_bd(log: Log) -> None:
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO log (description) VALUES ('{log.description}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_log_bd() -> list:    
    conn = psycopg2.connect(dados_conexao())
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log")
    linhas = cursor.fetchall()   
    logs = []
    for linha in linhas:
        datetime = linha[1].strftime("%d/%m/%Y") + ' - ' + str(linha[2])
        log = Log(linha[0], datetime, linha[3])         
        logs.append(log)
    cursor.close()
    conn.close()
    return logs