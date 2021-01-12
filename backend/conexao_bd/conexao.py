import psycopg2

  
def dados_conexao() -> str:
    host = 'pgsql08-farm15.uni5.net'
    user = 'topskills6'
    password = 'olist123'
    database = 'topskills6'
    connection = f'host={host} user={user} dbname={database} password={password}'
    return connection
        

    
    
