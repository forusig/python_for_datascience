import psycopg2


def connection_pgadmin() :
    connection = psycopg2.connect(
           dbname = "cakap_2",
            user = "postgres",
            password = "root",
            host = "localhost",
            port = "5432"
    )
    return connection