# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 07:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0012_auto_20180423_1007'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hero',
            options={'verbose_name': 'Hero', 'verbose_name_plural': 'Hero cabezera'},
        ),
        migrations.AlterModelOptions(
            name='modulocodigo',
            options={'verbose_name': 'Codigo', 'verbose_name_plural': 'Codigos'},
        ),
        migrations.AlterModelOptions(
            name='moduloimagen',
            options={'verbose_name': 'Imagen', 'verbose_name_plural': 'Imagenes'},
        ),
        migrations.AlterModelOptions(
            name='moduloitem',
            options={'verbose_name': 'Item de Producto', 'verbose_name_plural': 'Items de Productos'},
        ),
        migrations.AlterModelOptions(
            name='moduloitem2',
            options={'verbose_name': 'Item de Precio', 'verbose_name_plural': 'Items de Precios'},
        ),
        migrations.AlterModelOptions(
            name='modulonoticia',
            options={'verbose_name': 'Noticia', 'verbose_name_plural': 'Noticias de la p\xe1gina'},
        ),
        migrations.AlterModelOptions(
            name='modulopie',
            options={'verbose_name': 'Pie', 'verbose_name_plural': 'Pie de la p\xe1gina'},
        ),
        migrations.AlterModelOptions(
            name='moduloprecios',
            options={'verbose_name': 'Precio', 'verbose_name_plural': 'Precios'},
        ),
        migrations.AlterModelOptions(
            name='moduloproductos',
            options={'verbose_name': 'Producto', 'verbose_name_plural': 'Productos'},
        ),
        migrations.AlterField(
            model_name='moduloprecios',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
    ]
