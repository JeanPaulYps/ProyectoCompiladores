from flask import Flask, render_template, request, url_for, redirect
from Lexico import Lexico
from Analizador import Analizador

app = Flask(__name__)

@app.route('/',methods=['GET'])
def inicioPagina():
    return render_template("inicio.html")

@app.route('/lexico',methods=['GET','POST'])
def enviarPagina():
    if request.method == "POST":
        codigo = request.form['codigo']
        tokens = Lexico(codigo).tokens
        return render_template("tokens.html", tokens = tokens)
    else:
        return render_template("inicio_lexico.html")

@app.route('/sintactico',methods=['GET','POST'])
def analizador():
    if request.method == "POST":
        codigo = request.form['codigo']
        lexico = Lexico(codigo)
        analizador = Analizador(Analizador.leerTablaTAS("tablaTAS.csv"), lexico)
        analizador.analizar()
        return render_template("analizador.html", estados = analizador.estados)
    else:
        return render_template("inicio_analizador.html")
