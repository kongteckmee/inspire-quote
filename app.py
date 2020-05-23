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


@app.route('/insert_inspire', methods=['POST'])
def insert_inspire():
    inspires = mongo.db.quote
    inspires.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/edit_inspire/<quote_id>')
def edit_inspire(quote_id):
    the_quote = mongo.db.quote.find_one({"_id": ObjectId(quote_id)})
    all_category = mongo.db.category.find()
    return render_template("edit_inspire.html", quote=the_quote, categories=all_category)


@app.route('/update_inspire/<quote_id>', methods=['POST'])
def update_inspire(quote_id):
    quotes = mongo.db.quote
    quotes.update({'_id': ObjectId(quote_id)},
    {
        'quote': request.form.get('quote'),
        'category_name': request.form.get('category_name'),
        'description': request.form.get('description'),
        'quote_by': request.form.get('quote_by')
    })
    return redirect(url_for('index'))


@app.route('/delete_inspire/<quote_id>')
def delete_inspire(quote_id):
    mongo.db.quote.remove({"_id": ObjectId(quote_id)})
    return redirect(url_for('index'))


@app.route('/category')
def category():
    return render_template("category.html", categories=mongo.db.category.find())


@app.route('/add_category')
def add_category():
    return render_template("add_category.html")


@app.route('/insert_category', methods=['POST'])
def insert_category():
    category = mongo.db.category
    category.insert_one(request.form.to_dict())
    return redirect(url_for('category'))


@app.route('/edit_category/<category_id>')
def edit_category(category_id):
    the_category = mongo.db.category.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=the_category)


@app.route('/update_category/<category_id>', methods=['POST'])
def update_category(category_id):
    mongo.db.category.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('category'))


@app.route('/delete_category/<category_id>')
def delete_category(category_id):
    mongo.db.category.remove({"_id": ObjectId(category_id)})
    return redirect(url_for('category'))


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
