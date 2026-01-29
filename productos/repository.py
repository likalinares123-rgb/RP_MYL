from db import get_connection

def crear_tabla_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            descripción TEXT NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def obtener_clientes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, descripción FROM productos ORDER BY id DESC")
    datos = cur.fetchall()
    cur.close()
    conn.close()
    return datos
