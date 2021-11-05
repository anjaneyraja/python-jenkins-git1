import json
from unittest import TestCase
from mypage2 import  app

class ProductTest(TestCase):
    def test_welcome(self):
        with app.test_client() as c:
            resp = c.get('/api/products')
            self.assertEqual(resp.status_code, 200)

            self.assertEqual(json.loads(resp.get_data()),
                             [{"price": 20000, "productId": 1, "productName": "Iphone", "rating": 3.8},
                              {"price": 50000, "productId": 2, "productName": "Oneplus", "rating": 4.2},
                              {"price": 10000, "productId": 3, "productName": "MotoG", "rating": 4},
                              {"price": 15000, "productId": 4, "productName": "Nokia4", "rating": 3.6},
                              {"price": "5000", "productId": "5", "productName": "lava3", "rating": "5"}]
                             )

