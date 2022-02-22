import certifi
import dotenv
from pymongo import MongoClient
from bson import ObjectId
# from dotenv import load_dotenv

username = 'dev'
password = '24y1d75qt0XecszD'
cluster = 'cluster0.9ivx5.mongodb.net'

mongoDB = MongoClient(f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority", tlsCAFile=certifi.where())

db = mongoDB.UnitTest

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid objectid')
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type='string')
