from operator import mod
from unicodedata import name
from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=100)

class Topping(models.Model):
    name = models.TextField()
    pizza = models.ForeignKey(Pizza , models.CASCADE)

