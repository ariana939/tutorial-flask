from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
        <a href='/hola'>hola</a> 
        <a href='/chau'>chau</a> 
        <a href='/llamar'>llamar</a>
        """


@app.route("/hola")
def saludar():
    return "<p>hola</p>"

@app.route("/hola/<string:nombre>")
def saludar_con_nombre(nombre):
    return f"<p>hola {nombre}!</p>"

@app.route("/dado/<int:caras>")
def dado (caras):
    from random import randint
    numero = randint(1,caras)
    return f"<p>dado de {caras} caras, salio {numero}!</p>"

@app.route("/sumar/<int:n1>/<int:n2>")#ruta con argumento
def suma(n1, n2):
    suma = n1+n2
    return f"<p>{n1} mas {2} da {suma}</p>"


@app.route("/chau")
def despedir ():
    return "<p>chau</p>"



@app.route("/llamar/<string:nombre>") #el que hice yo
def llamar (nombre):
    return f"<p> {nombre}!</p>"


#dos rutas, dos links