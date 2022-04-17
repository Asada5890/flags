from random import randint
from flask import Flask

app = Flask(__name__)

# route - путь
@app.route("/")
def index():
    number = randint(1, 6)
    return f"<h1>Вы бросили кубик, выпало {number}</h1>"

app.run()
