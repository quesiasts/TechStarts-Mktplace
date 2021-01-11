import psycopg2

_host = 'pgsql08-farm15.uni5.net'
_user = 'topskills6'
_password = 'olist123'
_database = 'topskills6'

connection = f'host={_host} user={_user} dbname={_database} password={_password}'


def criar_produto_bd(nome:str, descricao:str, preco: float) -> None:
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute(f"""INSERT INTO product (name, description, price) 
                   VALUES ('{nome}', '{descricao}', '{preco}');""")
    conn.commit()
    cursor.close()
    conn.close()
    
    
def listar_produto_bd() -> list:
    products = []
    conn = psycopg2.connect(connection)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM product")
    prod = cursor.fetchall()
    for i in prod:
        i = {'nome': i[1],
            'descricao': i[2],
            'preco': i[3]
            }
        products.append(i)
    cursor.close()
    conn.close()
    return products
