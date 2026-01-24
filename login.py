from flask import Blueprint, render_template, redirect, url_for, request

login_bp = Blueprint("login", __name__)

# 🟢 Mostrar login
@login_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

# 🟢 Ingresar (por ahora sin validar)
@login_bp.route("/ingresar", methods=["POST"])
def ingresar():
    # más adelante acá validarás usuario y password
    return redirect(url_for("home"))
