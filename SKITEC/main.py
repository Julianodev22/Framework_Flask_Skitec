from flask import Flask, make_response
from markupsafe import escape
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/cadastro/usuario")
def usuario():
    return render_template("usuario.html")


@app.route("/cadastro/cadastro_user", methods=["POST"])
def cadastro_user():
    return request.form


@app.route("/cadastro/anuncio")
def anuncio():
    return render_template("anuncio.html")


@app.route("/cadastro/cadastro_anuncio", methods=["POST"])
def cadastro_anuncio():
    return request.form


@app.route("/fazer/perguntas")
def perguntas():
    return render_template("perguntas.html")


@app.route("/fazer/fazer_perguntas", methods=["POST"])
def fazer_perguntas():
    return request.form


@app.route("/anuncio/comprar")
def comprar():
    return render_template("comprar.html")


@app.route("/anuncio/realizar_compra", methods=["POST, GET"])
def realizar_compra():
    return request.form


@app.route("/relatorios")
def relatorios():
    return render_template("relatorios.html")


@app.route("/relatorios/emitir_vendas", methods=["POST, GET"])
def emitir_vendas():
    return request.form


if __name__ == "__main__":
    app.run()

# py -3 -m venv .venv
# .venv\scripts\activate
# pip install mysqlclient
# pip install mysql-connector-python
# pip install pymysql
