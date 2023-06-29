from django.db import models


class Cryptos(models.Model):
    name = models.TextField(max_length=10)
    price = models.FloatField(max_length=256)
    time = models.DateTimeField(auto_now_add=False) 
      