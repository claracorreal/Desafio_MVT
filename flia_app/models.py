from django.db import models
from datetime import datetime, date

class Familia(models.Model):
    nombre = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumple = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    email = models.EmailField()

