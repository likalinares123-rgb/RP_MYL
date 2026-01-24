from flask import Blueprint, render_template
from clientes_db import crear_tabla_clientes

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

# 👇 Se ejecuta una sola vez al iniciar
crear_tabla_clientes()

# 🟢 LISTADO
@clientes_bp.route("/")
def listado_clientes():
    return render_template("clientes.html")

# 🟢 FORMULARIO (opcional, ya lo tenés en otro blueprint)
@clientes_bp.route("/nuevo")
def nuevo():
    return render_template("clientes_form.html")
