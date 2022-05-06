from settings import app
import requests
import unittest


class BaseCase(unittest.TestCase):
    def setUp(self):
        self.app = app


class TestCreate(BaseCase):
    def test_successful_create(self):
        article = {"name": "Stylo",
                   "description": "Ecrit sur une feuille", "prix": 10}
        response = requests.post(
            "http://127.0.0.1:1234/article", headers={"Content-Type": "application/json"}, json=article)
        created = response.json()
        find = requests.get(
            "http://127.0.0.1:1234/article/"+str(created.get('id')), headers={"Content-Type": "application/json"})
        self.assertEqual(201, response.status_code)
        self.assertEqual(find.json(), created)


class TestGet(BaseCase):
    def test_successful_get(self):
        response = requests.get(
            "http://127.0.0.1:1234/article", headers={"Content-Type": "application/json"})
        print(len(response.json()))
        self.assertEqual(200, response.status_code)
        self.assertGreater(len(response.json()), 0)


class TestPut(BaseCase):
    def test_successful_put(self):
        article = {"name": "UpdatedStylo",
                   "description": "Ecrit sur une feuille", "prix": 10}
        response = requests.put(
            "http://127.0.0.1:1234/article/40", headers={"Content-Type": "application/json"}, json=article)
        updated = requests.get(
            "http://127.0.0.1:1234/article/40", headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.json(), updated.json())


class TestGetID(BaseCase):
    def test_successful_get(self):
        article = {
            "description": "Ecrit sur une feuille",
            "id": 50,
            "name": "Stylo",
            "prix": 10
        }
        response = requests.get(
            "http://127.0.0.1:1234/article/50", headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)
        self.assertEqual(article, response.json())


class TestDelete(BaseCase):
    def test_delete(self):
        response = requests.delete(
            "http://127.0.0.1:1234/article/57", headers={"Content-Type": "application/json"})
        article = self.test_successful_delete()
        self.assertEqual(article, 'None')

    def test_successful_delete(self):
        response = requests.get(
            "http://127.0.0.1:1234/article/57", headers={"Content-Type": "application/json"})
        return response.json()
