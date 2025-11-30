from flask import Flask, render_template, jsonify
import random


app = Flask(__name__)

from jugadores import JUGADORES_POPULARES


# Opcional: lista de nombres que podemos usar (si quieres siempre "Pedri",
# reemplaza random.choice(...) por "Pedri" más abajo)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roles/<int:cantidad>")
def roles(cantidad):
    # Asegurar mínimo 3 y máximo 6
    cantidad = max(3, min(cantidad, 6))

    # Elegir el nombre que tendrán todos los jugadores "normales".
    # Si quieres forzar Pedri, cambia la línea siguiente por: nombre_real = "Pedri"
    nombre_real = random.choice(JUGADORES_POPULARES)

    # Crear lista con (cantidad - 1) nombres iguales y 1 impostor
    listado = [nombre_real] * (cantidad - 1)
    listado.append("IMPOSTOR")

    # Mezclar la lista para que la posición del impostor sea aleatoria
    random.shuffle(listado)

    return jsonify(listado)

if __name__ == "__main__":
    app.run(debug=True)
