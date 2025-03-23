import mysql.connector
from flask import Flask, request

app = Flask(__name__)

# Conectar a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="ecologia"
)
cursor = conexion.cursor()

@app.route("/")
def index():
    return """
    <form action="/enviar" method="POST">
        <label for='nombre'>Nombre:</label>
        <input type='text' id='nombre' name='nombre' required>
        
        <label for='email'>Email:</label>
        <input type='email' id='email' name='email' required>

        <label for='mensaje'>Mensaje:</label>
        <textarea id='mensaje' name='mensaje'></textarea>

        <button type='submit'>Enviar</button>
    </form>
    """

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    email = request.form["email"]
    mensaje = request.form["mensaje"]

    # Insertar en la base de datos
    sql = "INSERT INTO mensajes (nombre, email, mensaje) VALUES (%s, %s, %s)"
    valores = (nombre, email, mensaje)
    cursor.execute(sql, valores)
    conexion.commit()

    return "Formulario enviado y guardado en la base de datos"

if __name__ == "__main__":
    app.run(debug=True)
