from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from OrganicMarketplace.Aplicaciones.Producto.models import Producto


class Productor(models.Model):
    descripcion = models.TextField(max_length=10000, null=True)
    direccion = models.CharField(max_length=1000)
    telefono = models.CharField(max_length=1000)
    latitud = models.FloatField(null=True)
    longitud = models.FloatField(null=True)
    extension = models.CharField(max_length=1000, null=True)
    usuarioId = models.OneToOneField(User)


class Productor_Producto(models.Model):
    productor = models.ForeignKey(Productor)
    producto = models.ForeignKey(Producto)
