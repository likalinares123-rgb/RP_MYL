from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
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
                ("Pedro", "pedro@mail.com"),
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

# 🟢 HOME (PANEL PRINCIPAL)
@app.route("/")
def home():
    return render_template("home.html")

# 🟢 CLIENTES (YA EXISTENTE)
@app.route("/clientes")
def clientes():
    lista = obtener_clientes()
    return render_template("clientes.html", clientes=lista)

# 🔹 PLACEHOLDERS (para después)
@app.route("/empresas")
def empresas():
    return "<h1>Empresas</h1><p>Próximamente...</p><a href='/'>Volver</a>"

@app.route("/productos")
def productos():
    return "<h1>Productos</h1><p>Próximamente...</p><a href='/'>Volver</a>"
