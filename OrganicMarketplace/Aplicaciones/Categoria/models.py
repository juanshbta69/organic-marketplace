from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(max_length=10000, null=True)
