# wsgi.py
from flask import Flask
from flask import jsonify
from flask import abort
from flask import Response
app = Flask(__name__)


the_products = [
    {'id': 1, 'name': 'Skello'},
    {'id': 2, 'name': 'Socialive.tv'},
    {'id': 3, 'name': 'plop'},
    {'id': 4, 'name': 'bidule'}
]

the_products_dic = {
    1: {'id': 1, 'name': 'Skello'},
    2: {'id': 2, 'name': 'Socialive.tv'},
    3: {'id': 3, 'name': 'plop'},
    4: {'id': 4, 'name': 'bidule'}
}


@app.route('/', methods=['GET'])
def hello():
    return "Hello  !!!"


@app.route('/api/v1/products', methods=['GET'])
def getProducts():
    return jsonify(the_products), 200


@app.route('/api/v1/products/<int:id>', methods=['GET'])
def getAProduct(id):
    if id in the_products_dic:
        return jsonify(the_products_dic[id]), 200
    else:
        abort(Response(f"product id:{id} not found ", 404) )


@app.route('/api/v1/products/:id', methods=['DELETE'])
def delProducts():
    return None, 500


@app.route('/api/v1/products', methods=['POST'])
def createProducts():
    return None, 500


@app.route('/api/v1/products/:id', methods=['PATCH'])
def updateProducts():
    return None, 500
