import os
from os import path
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo, pymongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_URI"] = os.getenv('MONGO_URI')
app.config["SECRET_KEY"] = os.getenv('SECRET_KEY')
DBS_NAME = "inspire_quote"

mongo = PyMongo(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", quotes=mongo.db.quote.find())


@app.route('/new_inspire')
def new_inspire():
    return render_template("new_inspire.html", categories=mongo.db.category.find())


@app.route('/category')
def category():
    return render_template("category.html", categories=mongo.db.category.find())


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
