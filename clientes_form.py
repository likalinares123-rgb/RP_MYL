from flask import Blueprint, render_template, request, redirect
from db import get_connection

clientes_form_bp = Blueprint("clientes_form", __name__)

@clientes_form_bp.route("/clientes/nuevo", methods=["GET", "POST"])
def nuevo_cliente():
    if request.method == "POST":
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

        return redirect("/clientes")

    return render_template("clientes_form.html")
