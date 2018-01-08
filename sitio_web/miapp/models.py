from django.db import models
from pymongo import MongoClient

client = MongoClient()
db = client.test   #base de datos
hamlet = db.hamlet #coleccion
