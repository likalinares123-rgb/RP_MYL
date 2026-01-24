from flask import Blueprint, render_template, request, redirect
from clientes_db import crear_tabla_clientes

clientes_bp = Blueprint("clientes", __name__, url_prefix="/clientes")

# 👇 Esto se ejecuta UNA vez cuando arranca Flask
crear_tabla_clientes()

# 🟢 LISTADO
@clientes_bp.route("/")
def listado():
    return render_template("clientes.html")

# 🟢 FORMULARIO
@clientes_bp.route("/nuevo")
def nuevo():
    return render_template("clientes_form.html")

