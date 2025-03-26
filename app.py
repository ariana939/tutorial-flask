from flask import Flask

app = Flask(__name__)

@app.route("/")
def principal():
    return """
        <a href='/hola'>hola</a> 
        <a href='/chau'>chau</a> 
        """


@app.route("/hola")
def hello_world():
    return "<p>hola</p>"

@app.route("/chau")
def despedir ():
    return "<p>chau</p>"

#dos rutas, dos links