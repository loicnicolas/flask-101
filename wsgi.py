# wsgi.py
from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello  !!!"

@app.route('/api/v1/products')
def getProducts():
    the_products = [
        { 'id': 1, 'name': 'Skello' },
        { 'id': 2, 'name': 'Socialive.tv' }
    ]
    return jsonify(the_products)
