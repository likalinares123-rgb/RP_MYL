from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection
from clientes_db import crear_tabla_clientes


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
    clientes = obtener_clientes()   
    return render_template("clientes.html", clientes=clientes)

# 🟢 FORMULARIO (ya lo usás desde el otro blueprint)
@clientes_bp.route("/nuevo")
def nuevo():
    return render_template("clientes_form.html")

@clientes_bp.route("/eliminar/<int:id>")
def eliminar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM clientes WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("clientes.listado_clientes"))


@clientes_bp.route("/editar/<int:id>")
def editar_cliente(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, nombre, email FROM clientes WHERE id = %s",
        (id,)
    )
    cliente = cur.fetchone()
    cur.close()
    conn.close()

    return render_template("clientes_form.html", cliente=cliente)

@clientes_bp.route("/actualizar/<int:id>", methods=["POST"])
def actualizar_cliente(id):
    nombre = request.form["nombre"]
    email = request.form["email"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE clientes SET nombre = %s, email = %s WHERE id = %s",
        (nombre, email, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("clientes.listado_clientes"))
