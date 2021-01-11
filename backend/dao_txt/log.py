from pathlib import Path
from datetime import datetime


_path_log = 'dados/logs.txt'

def criar_log(operacao: str) -> None:
    log_file = open(_path_log, 'a')
    dataHora = datetime.now()
    dataHora = dataHora.strftime("%d/%m/%Y - %H:%M:%S")
    log_file.write(f'{dataHora}; {operacao}\n')
    log_file.close()

def listar_log() -> list:
    lst_log = []
    file = Path(_path_log)
    if file.is_file():
        log_file = open(_path_log, 'r')
        for log in log_file:
            aux = log.split(';')
            log = {'datahora': aux[0], 'operacao': aux[1]}
            lst_log.append(log)
        log_file.close()
        return lst_log
    else:
        return []