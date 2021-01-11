import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills6'
_password = 'olist123'
_database = 'topskills6'

connection = f'host={_host} user={_user} dbname={_database} password={_password}'

def criar_log_bd(operacao: str) -> None:
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO log (description) VALUES ('{operacao}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_log_bd() -> list:
    logs = []
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM log")
    log = cursor.fetchall()
    for l in log:
        l = {'datahora': str(l[1].strftime("%d/%m/%Y")) + ' - ' + str(l[2]), 'operacao': l[3]}
        logs.append(l)
    cursor.close()
    conn.close()
    return logs