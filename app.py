from flask import Flask, request, render_template

app = Flask('indexhtml')

@app.route("/")
def index():
    return render_template("index.html")  # Asegúrate de que tu HTML está en la carpeta "templates"

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    email = request.form["email"]
    mensaje = request.form["mensaje"]

    # Aquí puedes guardar los datos en una base de datos o enviarlos por correo
    print(f"Nuevo mensaje de {nombre} ({email}): {mensaje}")

    return "Formulario enviado con éxito"

if __name__ == "__main__":
    app.run(debug=True)
