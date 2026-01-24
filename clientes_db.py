from db import get_connection

def crear_tabla_clientes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100),
        email VARCHAR(100)
    )
    """)

    conn.commit()
    cur.close()
    conn.close()


def insertar_cliente(nombre, email):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO clientes (nombre, email) VALUES (%s, %s)",
        (nombre, email)
    )

    conn.commit()
    cur.close()
    conn.close()


def obtener_clientes():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT id, nombre, email FROM clientes ORDER BY id DESC")
    clientes = cur.fetchall()

    cur.close()
    conn.close()
    return clientes


