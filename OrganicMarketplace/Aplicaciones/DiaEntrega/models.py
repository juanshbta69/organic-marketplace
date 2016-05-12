from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class DiaEntrega(models.Model):
    usuarioId = models.ForeignKey(User)
    diaSemana = models.CharField(max_length=100)
    numDia = models.IntegerField()
