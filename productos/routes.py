from flask import Blueprint, render_template, request, redirect, url_for
from productos.repository import (
    crear_tabla_productos,
    obtener_productos,
    insertar_producto
)

productos_bp = Blueprint(
    "productos",
    __name__,
    url_prefix="/productos"
)

# crear tabla al iniciar
crear_tabla_productos()

@productos_bp.route("/")
def listado():
    productos = obtener_productos()
    return render_template("productos/list.html", productos=productos)

@productos_bp.route("/nuevo")
def nuevo():
    return render_template("productos/form.html")

@productos_bp.route("/guardar", methods=["POST"])
def guardar():
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    insertar_producto(nombre, precio)
    return redirect(url_for("productos.listado"))
