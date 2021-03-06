# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-09 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('UnidadMedida', '__first__'),
        ('Categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('descripcion', models.TextField(max_length=10000, null=True)),
                ('imagen', models.ImageField(upload_to='photos')),
                ('cantidadMinima', models.FloatField()),
                ('unidadMedida', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='UnidadMedida.UnidadMedida')),
            ],
        ),
        migrations.CreateModel(
            name='Producto_Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Categoria.Categoria')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Producto.Producto')),
            ],
        ),
    ]
