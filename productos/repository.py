from db import get_connection

def crear_tabla_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id SERIAL PRIMARY KEY,
            nombre VARCHAR(100) NOT NULL,
            precio NUMERIC(10,2) NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

def obtener_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, precio FROM productos ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def insertar_producto(nombre, precio):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO productos (nombre, precio) VALUES (%s, %s)",
        (nombre, precio)
    )
    conn.commit()
    cur.close()
    conn.close()
