from flask import Blueprint, render_template
from clientes_db import crear_tabla_clientes
from db import get_connection

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

# 👇 Se ejecuta una sola vez al iniciar
crear_tabla_clientes()

# 🔹 Función para traer clientes desde Postgres
def obtener_clientes():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, email FROM clientes ORDER BY id DESC")
    clientes = cur.fetchall()
    cur.close()
    conn.close()
    return clientes

# 🟢 LISTADO
@clientes_bp.route("/")
def listado_clientes():
    clientes = obtener_clientes()   # 👈 ESTO FALTABA
    return render_template("clientes.html", clientes=clientes)

# 🟢 FORMULARIO (ya lo usás desde el otro blueprint)
@clientes_bp.route("/nuevo")
def nuevo():
    return render_template("clientes_form.html")
