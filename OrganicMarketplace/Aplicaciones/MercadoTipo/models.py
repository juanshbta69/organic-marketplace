from __future__ import unicode_literals

from django.db import models

# Create your models here.
from OrganicMarketplace.Aplicaciones.Producto.models import Producto


class MercadoTipo(models.Model):
    nombre = models.CharField(max_length=1000)
    descripcion = models.TextField(max_length=10000, null=True)
    imagen = models.ImageField(upload_to='photos')
    precio = models.FloatField()
    estado = models.CharField(max_length=100)


class MercadoTipo_Producto(models.Model):
    mercadoTipo = models.ForeignKey(MercadoTipo)
    producto = models.ForeignKey(Producto)
    cantidad = models.IntegerField()
