from flask import Flask
import sqlite3

app = Flask(__name__)

def obtener_clientes():
    conn = sqlite3.connect("clientes.db")
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, email FROM clientes")
    clientes = cursor.fetchall()
    conn.close()
    return clientes

@app.route("/")
def listar_clientes():
    clientes = obtener_clientes()
    html = "<h1>Listado de clientes</h1><ul>"
    for nombre, email in clientes:
        html += f"<li>{nombre} - {email}</li>"
    html += "</ul>"
    return html

