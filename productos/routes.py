from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection
from productos.repository import crear_tabla_productos


productos_bp = Blueprint("productos", __name__, url_prefix="/productos")

# 👇 Se ejecuta una sola vez al iniciar
crear_tabla_productos()

# 🔹 Función para traer productos desde Postgres
def obtener_productos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nombre, descripcion FROM productos ORDER BY id DESC")
    productos = cur.fetchall()
    cur.close()
    conn.close()
    return productos

# 🟢 LISTADO
@productos_bp.route("/")
def listado_productos():
    productos = obtener_productos()   
    return render_template("productos/list.html", productos=productos)

# 🟢 FORMULARIO (ya lo usás desde el otro blueprint)
@productos_bp.route("/nuevo")
def nuevo():
    return render_template("productos/form.html")

@productos_bp.route("/eliminar/<int:id>")
def eliminar_productos(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM productos WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("productos.listado_productos"))


@productos_bp.route("/editar/<int:id>")
def editar_productos(id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "SELECT id, nombre, descripcion FROM productos WHERE id = %s",
        (id,)
    )
    producto = cur.fetchone()
    cur.close()
    conn.close()

    return render_template("productos/form.html", producto=producto)

@productos_bp.route("/actualizar/<int:id>", methods=["POST"])
def actualizar_producto(id):
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]

    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE productos SET nombre = %s, descripcion = %s WHERE id = %s",
        (nombre, descripcion, id)
    )
    conn.commit()
    cur.close()
    conn.close()

    return redirect(url_for("productos.listado_productos"))
