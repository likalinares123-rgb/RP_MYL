import os
import psycopg2

def get_connection():
    database_url = os.environ.get("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL no está configurada")

    return psycopg2.connect(database_url)

