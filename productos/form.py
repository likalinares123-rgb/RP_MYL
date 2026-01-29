from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import get_connection

productos_form_bp = Blueprint(
    "productos_form",
    __name__,
    url_prefix="/productos"
)

# 🟢 Mostrar formulario
@productos_form_bp.route("/nuevo", methods=["GET"])
def nuevo_producto():
    return render_template("productos/form.html")

# 🟢 Guardar 
@productos_form_bp.route("/guardar", methods=["POST"])
def guardar_producto():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO productos (nombre, descripcion) VALUES (%s, %s)",
        (nombre, descripcion)
    )
    conn.commit()
    cur.close()
    conn.close()

 

    return redirect(url_for("productos.listado_productos"))
