from flask import Flask, render_template, url_for,request,redirect,abort

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template('home.html', nombre="Juana", apellido="Rehl")

@app.route("/Datos_personales", methods=["GET", "POST"])
def Formulario():
    if request.method=="POST":
        nombre=request.form.get("fnombre")
        apellido=request.form.get("fapellido")
        celular=request.form.get("fcelular")
        direccion=request.form.get("fdirec")
        dni=request.form.get("fdni")
        return redirect(url_for('Aceptado', nombre=nombre, apellido=apellido,celular=celular,direccion=direccion,dni=dni))
    return render_template('formulario.html')

@app.route("/aceptado/<nombre>/<apellido>/<celular>/<direccion>/<dni>")
def Aceptado(nombre, apellido,celular,direccion,dni):
    return render_template('aceptado.html',lista=[nombre,apellido,celular,direccion,dni] )

if __name__ == "__main__":
   app.run("127.0.0.1", port="8000", debug=True)
