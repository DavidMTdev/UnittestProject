
import requests
from unittest import TestCase
from fastapi import status
from bson import ObjectId

from app.models.article import Article

class TestApi(TestCase):
    
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/articles'
        self.data = {
            "name": "My Test",
            "price": 1000.99,
            "type": "Test RTX 7000",
            "memoryCapacity": 24,
            "memoryType": "GDDR8"
        }
        self.dataUpdated = {
            "name": "My Test",
            "price": 555.99,
            "type": "GeForce RTX 3090",
            "memoryCapacity": 8,
            "memoryType": "GDDR5"
        }

        self.reqCreated = requests.post(self.url, json=self.data)
        self.newArticle = Article(**self.reqCreated.json())

        self.reqGetAll = requests.get(f'{self.url}/')
        self.articles = [Article(**article) for article in self.reqGetAll.json()]

        self.reqGetbyId = requests.get(f'{self.url}/{self.newArticle.id}')
        self.article = Article(**self.reqGetbyId.json())

        self.reqUpdated = requests.put(f'{self.url}/{self.newArticle.id}', json=self.dataUpdated)
        self.reqGetAfterUpdate = requests.get(f'{self.url}/{self.newArticle.id}')

        self.articleAfterUpdate = Article(**self.reqGetAfterUpdate.json())

        self.reqDeleted = requests.delete(f'{self.url}/{self.newArticle.id}')
        self.reqGetAfterDelete = requests.get(f'{self.url}/{self.newArticle.id}')


    def teardown(self):
        pass

    def test_GetAll(self):
        self.assertIsInstance(self.articles, list)
        self.assertIsInstance(self.articles[0], Article)
        self.assertEqual(self.reqGetAll.status_code, status.HTTP_200_OK)

    def test_GetById(self):
        self.assertIsInstance(self.article, Article)
        self.assertIsInstance(self.article.id, ObjectId)

        self.assertEqual(self.article.name, self.data['name'])
        self.assertEqual(self.article.price, self.data['price'])
        self.assertEqual(self.article.memoryCapacity, self.data['memoryCapacity'])
        self.assertEqual(self.article.memoryType, self.data['memoryType'])
        self.assertEqual(self.reqGetbyId.status_code, status.HTTP_200_OK)

    def test_Created(self):
        self.assertIsInstance(self.newArticle, Article)
        self.assertIsInstance(self.newArticle.id, ObjectId)

        self.assertEqual(self.newArticle.name, self.data['name'])
        self.assertEqual(self.newArticle.price, self.data['price'])
        self.assertEqual(self.newArticle.memoryCapacity, self.data['memoryCapacity'])
        self.assertEqual(self.newArticle.memoryType, self.data['memoryType'])
        self.assertEqual(self.reqCreated.status_code, status.HTTP_201_CREATED)

    def test_Updated(self):
        self.assertIsInstance(self.articleAfterUpdate, Article)
        self.assertIsInstance(self.articleAfterUpdate.id, ObjectId)

        self.assertEqual(self.articleAfterUpdate.name, self.dataUpdated['name'])
        self.assertEqual(self.articleAfterUpdate.price, self.dataUpdated['price'])
        self.assertEqual(self.articleAfterUpdate.memoryCapacity, self.dataUpdated['memoryCapacity'])
        self.assertEqual(self.articleAfterUpdate.memoryType, self.dataUpdated['memoryType'])
        self.assertEqual(self.reqUpdated.status_code, status.HTTP_204_NO_CONTENT)

    def test_deleted(self):
        self.assertEqual(self.reqDeleted.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(self.reqGetAfterDelete.status_code, status.HTTP_404_NOT_FOUND)

