from django.db import models

class Phar(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, max_length=255)
    sideeffects = models.TextField(blank=True, max_length=255)
    image = models.CharField(max_length=2083)