from flask import Flask, render_template, request, url_for, redirect
from analizadorLexico import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/programa',methods=['GET','POST'])
def enviarPagina():
    if request.method == "POST":
        tokens = request.form['programa']
        print(tokens)
        TokensRegex = obtenerTokensRegex()
        codigo = open("prueba.txt",'r')
        codigo = codigo.read()
        lista = []
        for i in re.finditer(TokensRegex, codigo):
            lista.append((i, i.lastgroup))
        tokensFalsos = [
            ("variable", "a"),
            ("llave", "{"),
            ("llave", "}"),
            ("palabrasReservadas", "IF")
        ]
        return render_template("tokens.html", tokens = lista)
    else:
        return render_template("prueba.html")
