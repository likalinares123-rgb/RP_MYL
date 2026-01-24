from flask import Flask

app = Flask(__name__)

clientes = [
    {"nombre": "Ana", "email": "ana@mail.com"},
    {"nombre": "Luis", "email": "luis@mail.com"},
    {"nombre": "María", "email": "maria@mail.com"},
]

@app.route("/")
def listar_clientes():
    html = "<h1>Listado de clientes</h1><ul>"
    for c in clientes:
        html += f"<li>{c['nombre']} - {c['email']}</li>"
    html += "</ul>"
    return html
