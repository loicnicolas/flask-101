# tests/test_views.py
from flask_testing import TestCase
from flask import jsonify
from wsgi import app


class TestViews(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

#C
    def test_add_products_json(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        payload = {'id': 5, 'name': 'truc'}
        response = self.client.post("/api/v1/products", json=payload)
        self.assertEqual(response.status_code, 201)
        response = self.client.get("/api/v1/products/5")
        self.assertEqual(response.status_code, 200)


    def test_add_products_fail(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        payload = {'id': 4, 'name': 'truc'}
        response = self.client.post("/api/v1/products", json=payload)
        self.assertEqual(response.status_code, 406)

#R
    def test_products_json(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        response = self.client.get("/api/v1/products")
        products = response.json
        self.assertIsInstance(products, list)
        self.assertGreater(len(products), 3) # 3 is not a mistake here.
        self.assertEqual(response.status_code, 200)


    def test_products_id1_json(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        response = self.client.get("/api/v1/products/1")
        product = response.json
        self.assertIsInstance(product, object)
        self.assertEqual(response.status_code, 200)


    def test_products_id5_404(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        response = self.client.get("/api/v1/products/5")
        self.assertEqual(response.status_code, 404)
#U

    def test_update_product(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        payload = {'id': 4, 'name': 'truc2'}
        response = self.client.patch('/api/v1/products/4', json=payload)

        self.assertEqual(response.status_code, 204)

        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 200)
        product1 = response.json
        self.assertEqual(product1['id'], 1)
        self.assertEqual(product1['name'], 'Skello')

        response = self.client.get("/api/v1/products/4")
        self.assertEqual(response.status_code, 200)
        product4 = response.json
        self.assertEqual(product4['id'], 4)
        self.assertEqual(product4['name'], 'truc2')

#D
    def test_Del_products_id1(self):
        app.the_products_dic = {
            1: {'id': 1, 'name': 'Skello'},
            2: {'id': 2, 'name': 'Socialive.tv'},
            3: {'id': 3, 'name': 'plop'},
            4: {'id': 4, 'name': 'bidule'}
        }
        response = self.client.delete("/api/v1/products/1")
        self.assertEqual(response.status_code, 204)
        response = self.client.get("/api/v1/products/1")
        self.assertEqual(response.status_code, 404)


