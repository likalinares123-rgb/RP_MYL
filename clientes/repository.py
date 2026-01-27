from db import get_connection

def crear_tabla_clientes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def obtener_clientes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, email FROM clientes ORDER BY id DESC")
    datos = cur.fetchall()
    cur.close()
    conn.close()
    return datos
