from flask import Blueprint, render_template, redirect, url_for, request

login_bp = Blueprint("login", __name__, url_prefix="/login")

@login_bp.route("/", methods=["GET"])
def login():
    return render_template("login/login.html")

@login_bp.route("/ingresar", methods=["POST"])
def ingresar():
    return redirect(url_for("home"))
