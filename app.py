from flask import Flask, url_for
import sqlite3

app = Flask(__name__)

@app.route("/")
def principal():
    url_hola = url_for("saludar_con_nombre", nombre = "pepito")#ruta con argumento
    url_dado = url_for("dado", caras=6)#ruta con argumento
    url_logo = url_for("static", filename="img.webp")

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("despedir")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar dado</a>
    """
    


@app.route("/hola")#ruta comun, saluda como nosotros lo programamos
def saludar():
    return "<p>hola</p>" 

@app.route("/hola/<string:nombre>") #ruta con argumento, saluda con el nombre que le dan, si comienza con <> siginifca que va a ir algo
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
def despedir():
    return "<p>chau</p>"



@app.route("/llamar/<string:nombre>") #el que hice yo
def llamar (nombre):
    return f"<p> {nombre}!</p>"

#dos rutas, dos links


#-------------
def main ():
    url_hola = url_for("hello")
    url_dado = url_for("dado", caras=6)
    url_logo = url_for("static", filename="img/logo.png")

    return f"""
    <a href="{url_hola}">Hola</a>
    <br>
    <a href="{url_for("bye")}">Chau</a>
    <br>
    <a href="{url_logo}">Logo</a>
    <br>
    <a href="{url_dado}">Tirar dado</a>
    """
#-------------CONEXION A BASE DE DATOS---------------------------------#
db=None #variable vacia

def abrirConexion():
    global db  # llama 
    db = sqlite3.connect('instance/datos.sqlite') #abre lo que le ponemos dentro del parentesis
    db.row_factory = sqlite3.Row
    return db # devuelve

def cerrarConexion():
    global db #llama
    if db is not None:#preunta si no esta vacio
        db.close()#cierra
        db=None#vuelve a estar vacio

@app.route("/usuarios/")
def obterGente():
    global db 
    conexion = abrirConexion()
    cursor = conexion.cursor()
    cursor.execute('SELECT * FROM usuarios')
    resultado = cursor.fetchall()#fetchall es como el asterisco,selecciona todo en cambio el fetchone solo uno
    cerrarConexion()
    fila = [dict(row) for row in resultado] 
    return str(fila)

  







#tipos de ruta
#absoluto: con barra
#relativo: sin barra 




