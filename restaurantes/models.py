from django.db import models
from pymongo import MongoClient

client = MongoClient()
db = client.test #base de datos
restaurantes = db.restaurantes #coleccion
# Create your models here.
