from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=200)
    abreviatura = models.CharField(max_length=10)
