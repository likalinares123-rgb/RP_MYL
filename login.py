from flask import Blueprint, render_template, redirect, url_for, request

login_bp = Blueprint("login", __name__)

# 🟢 Mostrar login
@login_bp.route("/login", methods=["GET"])
def login():
    return render_template("login.html")

@login_bp.route("/ingresar", methods=["POST"])
def ingresar():
    # más adelante validás usuario/password
    return redirect("/home")

