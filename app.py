from flask import Flask, render_template, request, url_for, redirect
from analizadorLexico import *
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def enviarPagina():
    if request.method == "POST":
        codigo = request.form['codigo']
        tokens = obtenerTokens(codigo)
        return render_template("tokens.html", tokens = tokens)
    else:
        return render_template("prueba.html")
