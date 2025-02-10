from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def eventos():
    return render_template('ejemplohtmljava.html')

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html", year=2024) 

@app.route("/", methods=["GET", "POST"])
def hola():
    return render_template('hola.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

@app.route("/", methods=["GET", "POST"])
def form_a_otra_pag():
    if request.method=="POST":
        nombre=request.form.get("nombre")
        apellido=request.form.get("apellido")
        return redirect(url_for('nueva_pagina', nombre=nombre, apellido=apellido))
    return render_template('pruebaform.html')
    
@app.route("/nuevapag/<nombre>/<apellido>")
def nueva_pagina(nombre,apellido):
    lista=["Juana", "Taylor", "Boquita"]
    user="TTPD"
    return render_template('pruebaformredirect.html', nombre=nombre, apellido=apellido, lista=lista, user=user)


if __name__== "__main__":
    app.run("127.0.0.1", port="5001", debug=True)
    #127.0.0.1 el local code de tu maquina
