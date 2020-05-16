import os
from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/new_inspire')
def new_inspire():
    return render_template("new_inspire.html")


@app.route('/category')
def category():
    return render_template("category.html")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=os.environ.get("PORT"),
            debug=True)
