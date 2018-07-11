# wsgi.py
from flask import Flask
from flask import jsonify
from flask import abort
from flask import Response
from flask import request
app = Flask(__name__)


app.the_products_dic = {
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
    return jsonify(list(app.the_products_dic.values())), 200


@app.route('/api/v1/products/<int:id>', methods=['GET'])
def getAProduct(id):
    if id in app.the_products_dic:
        return jsonify(app.the_products_dic[id]), 200
    else:
        abort(Response(f"product id:{id} not found", 404) )


@app.route('/api/v1/products/<int:id>', methods=['DELETE'])
def delProducts(id):
    if id in app.the_products_dic:
        app.the_products_dic.pop(id)
    else:
        abort(Response(f"product id:{id} not found. Cannot be deleted", 404))

    return Response("Del ok.", 204)


@app.route('/api/v1/products', methods=['POST'])
def createProducts():
    # data = dict(request.get_json(force = True))
    data = request.get_json()
    if data['id'] not in app.the_products_dic:
        # app.the_products_dic.append(data['id'], data)
        app.the_products_dic.update({data['id'] : data})

    else:
        abort(Response(f"id {data['id']} already exists", 406))

    return Response("Create ok.", 201)


@app.route('/api/v1/products/<int:id>', methods=['PATCH'])
def updateProducts(id):
    return abort(500)
