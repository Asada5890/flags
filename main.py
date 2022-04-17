from random import randint
from flask import Flask, render_template

app = Flask(__name__)

# route - путь
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dice")
def dice():
    number = randint(1, 6)
    return render_template("dice.html", result=number)


app.run()
