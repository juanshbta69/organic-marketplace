from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Consumidor(models.Model):
    usuarioId = models.OneToOneField(User)
    direccion = models.CharField(max_length=1000)
    telefono = models.CharField(max_length=1000)