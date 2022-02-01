from flask import Flask, Blueprint, render_template, url_for, redirect
from model import db
import random

views = Blueprint(__name__, "views")

app = Flask(__name__)

app.register_blueprint(views, url_prefix="/")


@app.route("/index")
def homepage():
    card = random.choice(db)
    return render_template("index.html", card=card)


if __name__ == "__main__":
    app.run(debug=True, port=8000)
