from flask import Blueprint, render_template
import sqlite3
import os

clientes_bp = Blueprint("clientes", __name__)

DB_NAME = "clientes.db"

def init_db():
    if not os.path.exists(DB_NAME):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            email TEXT
        )
        """)
        cursor.executemany(
            "INSERT INTO clientes (nombre, email) VALUES (?, ?)",
            [
                ("Ana", "ana@mail.com"),
                ("Luis", "luis@mail.com"),
                ("María", "maria@mail.com"),
                ("Carlos", "carlos@mail.com"),
                ("Lucía", "lucia@mail.com"),
                ("Faban", "pedro@mail.com"),
            ]
        )
        conn.commit()
        conn.close()

def obtener_clientes():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, email FROM clientes")
    datos = cursor.fetchall()
    conn.close()
    return datos

@clientes_bp.route("/clientes")
def clientes():
    lista = obtener_clientes()
    return render_template("clientes.html", clientes=lista)
