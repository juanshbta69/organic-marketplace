from __future__ import unicode_literals

from django.db import models

# Create your models here.
from OrganicMarketplace.Aplicaciones.Categoria.models import Categoria
from OrganicMarketplace.Aplicaciones.UnidadMedida.models import UnidadMedida


class Producto(models.Model):
    unidadMedida = models.ForeignKey(UnidadMedida)
    nombre = models.CharField(max_length=1000)
    descripcion = models.TextField(max_length=10000, null=True)
    imagen = models.ImageField(max_length=10000, upload_to='photos')
    cantidadMinima = models.FloatField()
    premium = models.BooleanField(default=False)

class Producto_Categoria(models.Model):
    producto = models.ForeignKey(Producto)
    categoria = models.ForeignKey(Categoria)
