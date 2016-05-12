# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(max_length=10000, upload_to='photos'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='unidadMedida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='UnidadMedida.UnidadMedida'),
        ),
    ]
