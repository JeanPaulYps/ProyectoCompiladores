from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/programa',methods=['GET','POST'])
def enviarPagina():
    if request.method == "POST":
        print(request.form['programa'])
        return request.form['programa']
    else:
        return render_template("prueba.html")

@app.route('/tokens')
def enviarTokens():
    tokensFalsos = [
        ("variable", "a"),
        ("llave", "{"),
        ("llave", "}"),
        ("palabrasReservadas", "IF"),

    ]
    return render_template("tokens.html", tokens = tokensFalsos)