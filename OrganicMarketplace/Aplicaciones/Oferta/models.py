from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from OrganicMarketplace.Aplicaciones.Producto.models import Producto
from OrganicMarketplace.Aplicaciones.Productor.models import Productor


class Oferta(models.Model):
    productor = models.ForeignKey(Productor)
    admin = models.ForeignKey(User, null=True)
    producto = models.ForeignKey(Producto)
    fecha = models.DateField(auto_now_add=True)
    cantidad = models.IntegerField()
    precioUnitario = models.FloatField()
    total = models.FloatField()
    estado = models.CharField(max_length=50)
