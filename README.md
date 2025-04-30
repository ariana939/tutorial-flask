# tutorial-flask
python -m venv .venv
source .venv/bin/activate
pip install flask
flask --version

flask run: <!--corre normal
opciones para ver como se corre
flask run -h 0.0.0.0
flask run --debug <!--me permite ver lo errores y ver los cambios automaticamente 
flask run -p 5010 diferente 5000

crear carpeta


#tipos de ruta
#absoluto: con barra
#relativo: sin barra 

cursor.execute()
cursor.fetchone() <!-- proximo registro, devuelve uno solo
cursor.fetchall() <!-- todos los registros que quedan en una lista 

db.commit()<!--confirma los cambios>
db.cursor()<!--pide un cursor nuevo>
db.close()<!--cierra>
db.execute() <!--toma la consulta y parametros >

SQLITE:
delete from usuarios WHERE id = 2 <!-- le digo que usuario quiero borrar, si no pongo el WHERE se borra todo>

usr = 2
consulta = f"delete from usuarios WHERE id = {usr};"
consulta

user =2 OR 1=1
consulta = f"delete from usuarios WHERE id = {usr};"<!--borra todo, por eso no se usa la "f">
consulta

manera de como si hacer la consulta:
cursor = db.execute("delete from usuarios WHERE id=?", (usr,))<!-- siempre con un signo de pregunta y una tupla>
dir(cursor)


cursor sirve para ver los resultados
