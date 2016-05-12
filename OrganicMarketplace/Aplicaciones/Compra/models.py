from __future__ import unicode_literals

from django.db import models

# Create your models here.
from OrganicMarketplace.Aplicaciones.Consumidor.models import Consumidor
from OrganicMarketplace.Aplicaciones.MercadoTipo.models import MercadoTipo
from OrganicMarketplace.Aplicaciones.Producto.models import Producto


class Compra(models.Model):
    consumidor = models.ForeignKey(Consumidor)
    fecha = models.DateField(auto_now_add=True)
    totalCompra = models.FloatField()
    estado = models.CharField(max_length=100)


class Compra_Producto(models.Model):
    compra = models.ForeignKey(Compra)
    producto = models.ForeignKey(Producto, null=True)
    mercadoTipo = models.ForeignKey(MercadoTipo, null=True)
    cantidad = models.IntegerField()
    valor = models.FloatField()
