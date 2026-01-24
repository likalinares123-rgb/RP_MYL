from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_connection

clientes_form_bp = Blueprint(
    "clientes_form",
    __name__,
    url_prefix="/clientes"
)

# 🟢 Mostrar formulario
@clientes_form_bp.route("/nuevo", methods=["GET"])
def nuevo_cliente():
    return render_template("clientes_form.html")

# 🟢 Guardar cliente
@clientes_form_bp.route("/guardar", methods=["POST"])
def guardar_cliente():
    nombre = request.form["nombre"]
    email = request.form["email"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO clientes (nombre, email) VALUES (%s, %s)",
        (nombre, email)
    )
    conn.commit()
    cur.close()
    conn.close()

 

    return redirect(url_for("clientes.listado_clientes"))
