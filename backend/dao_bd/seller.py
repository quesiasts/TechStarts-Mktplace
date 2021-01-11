import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills6'
_password = 'olist123'
_database = 'topskills6'

connection = f'host={_host} user={_user} dbname={_database} password={_password}'

def criar_seller_bd(nome:str, email:str, telefone:str) -> None:
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO sellers (name, email, phone) VALUES ('{nome}', '{email}', '{telefone}');")
    conn.commit()
    cursor.close()
    conn.close()
    
def listar_seller_bd() -> list:
    sellers = []
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sellers")
    seller = cursor.fetchall()
    for s in seller:
        s = {'nome': s[1],
            'email': s[2],
            'telefone': s[3]
            }
        sellers.append(s)
    cursor.close()
    conn.close()
    return sellers