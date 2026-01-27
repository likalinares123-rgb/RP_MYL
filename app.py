from flask import Flask, render_template
from clientes.routes import clientes_bp
from clientes.form import clientes_form_bp
from login.routes import login_bp

app = Flask(__name__)
app.secret_key = "clave-secreta-temporal"  

# 🔗 Registrar módulo clientes
app.register_blueprint(clientes_bp)
app.register_blueprint(clientes_form_bp)
app.register_blueprint(login_bp) 

# 🟢 HOME (MENÚ PRINCIPAL)
@app.route("/")
def login():
    return render_template("login/login.html")


@app.route("/home")
def home():
    return render_template("home.html")


# 🔹 PLACEHOLDERS

@app.route("/empresas")
def empresas():
    return "<h1>Empresas</h1><p>Próximamente...</p><a href='/'>Volver</a>"

@app.route("/productos")
def productos():
    return "<h1>Productos</h1><p>Próximamente...</p><a href='/'>Volver</a>"

