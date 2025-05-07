from flask import Flask, url_for, render_template
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
#-------------CONEXION A BASE DE DATOS---------------------------------con thomi#
#db=None #variable vacia

#def abrirConexion():
#    global db  # llama 
#   db = sqlite3.connect('instance/datos.sqlite') #abre lo que le ponemos dentro del parentesis
#   db.row_factory = sqlite3.Row
#   return db # devuelve

#def cerrarConexion():
#    global db #llama
#    if db is not None:#preunta si no esta vacio
#       db.close()#cierra
#        db=None#vuelve a estar vacio

#@app.route("/usuarios/")
#def obterGente():
#    global db 
#    conexion = abrirConexion()
#    cursor = conexion.cursor()
#    cursor.execute('SELECT * FROM usuarios')
#    resultado = cursor.fetchall()#fetchall es como el asterisco,selecciona todo en cambio el fetchone solo uno
#    cerrarConexion()
#    fila = [dict(row) for row in resultado] 
#    return str(fila)
#------------------------------------------------30-4- navarro
db = None


def dict_factory(cursor, row):
  """Arma un diccionario con los valores de la fila."""
  fields = [column[0] for column in cursor.description]
  return {key: value for key, value in zip(fields, row)}


def abrirConexion():
   global db
   db = sqlite3.connect("instance/datos.sqlite")
   db.row_factory = dict_factory


def cerrarConexion():
   global db
   db.close()
   db = None


@app.route("/test-db")
def testDB():
   abrirConexion()
   cursor = db.cursor()
   cursor.execute("SELECT COUNT(*) AS cant FROM usuarios; ")
   res = cursor.fetchone()
   registros = res["cant"]
   cerrarConexion()
   return f"Hay {registros} registros en la tabla usuarios"

#actividades

#insertar un usuario nuevo 
@app.route("/insertar/<string:usuario>/<string:email>")#nombre, email
def insertar_usuario(usuario,email):
   abrirConexion()
   cursor = db.cursor()
   cursor = db.execute ("INSERT INTO usuarios(usuario, email) VALUES('mari', 'm@gmail.com');")
   cursor = db.commit()
   cerrarConexion()
   return f"se agrego a {usuario} y con el email {email} "

#borrar un usuario
@app.route("/borrar/<int:id>")#detalle/id
def borrar_usuario(id):
   abrirConexion()
   cursor = db.cursor()
   cursor = db.execute ("DELETE from usuarios WHERE id=?", (id,))
   cursor = db.commit()
   cerrarConexion()
   return f"se borro a id {id} en la tabla de usuarios"

#mostrar un usuario y un email
@app.route("/mostrar/<int:id>")#id
def mostrar_usuario(id):
   abrirConexion()
   cursor = db.cursor()
   cursor = db.execute ("SELECT usuario, email from usuarios WHERE id=?", (id,))
   resultado = cursor.fetchone()
   cerrarConexion()
   return f"usuario:{resultado['usuario']}    email:{resultado['email']}"

#cambiar el mail de un usuario elegido, no lo termine
@app.route("/cambiar/<string:usuario>/<string:email>")#nombre, email
def cambiar_email(usuario, email):
   abrirConexion()
   cursor = db.cursor()
   cursor = db.execute ("SELECT usuario, email from usuarios WHERE id=?")
   resultado = cursor.fetchone()
   cerrarConexion()
   return f"se le cambio el email a   quedo como :{resultado['usuario']}    email:{resultado['email']}"

#----------------------------------------------------------7-5-navarro
@app.route("/mostrar-datos-plantilla/<int:id>")
def datos_plantilla(id):
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT id, usuario, email, telefono, direccion FROM usuarios WHERE id = ?;", (id,))
    res = cursor.fetchone()
    cerrarConexion()
    usuario = None
    email= None
    telefono = None
    direccion = None
    if res != None:
       usuario=res['usuario']
       email=res['email']
       telefono=res['telefono']
       direccion=res['direccion']
    return render_template("datos.html", id=id, usuario=usuario, email=email, telefono=telefono, direccion=direccion)



@app.route("/mostar-datos-plantilla")
def lista_de_usuario():
    abrirConexion()
    cursor = db.cursor()
    cursor.execute("SELECT usuario FROM usuarios")
    res = cursor.fetchall()
    cerrarConexion()
    return render_template("listaDeUsuario.html", usuarios = [res])

@app.route("/usuarios")
def mostrar():
    url_datos1 = url_for("datos_plantilla", id=1)  
    url_datos2 = url_for("datos_plantilla", id=2)
    return f"""
        <a href="{url_datos1}">Andres</a>
        <br>
        <a href="{url_datos2}">Tomas</a>
    """









