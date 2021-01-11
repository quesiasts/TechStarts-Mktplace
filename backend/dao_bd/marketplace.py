import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills6'
_password = 'olist123'
_database = 'topskills6'

connection = f'host={_host} user={_user} dbname={_database} password={_password}'


def criar_marketplace_bd(nome:str, descricao:str) -> None:
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO marketplaces (marketplace_name, description) VALUES ('{nome}', '{descricao}');")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def listar_marketplace_bd() -> list:
    marketplaces = []
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM marketplaces")
    mkt = cursor.fetchall()
    for i in mkt:
        i = {'nome': i[1],
            'descricao': i[2]
            }
        marketplaces.append(i)
    cursor.close()
    conn.close()
    return marketplaces
