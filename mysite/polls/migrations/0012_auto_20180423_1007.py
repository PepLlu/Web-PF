# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 08:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0011_auto_20180423_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='hero',
            name='titulopost',
            field=models.CharField(default=2, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulocodigo',
            name='titulopost',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloimagen',
            name='titulopost',
            field=models.CharField(default=3, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloitem',
            name='titulopost',
            field=models.CharField(default=3, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloitem2',
            name='titulopost',
            field=models.CharField(default=3, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='modulonoticia',
            name='titulopost',
            field=models.CharField(default=4, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloprecios',
            name='titulopost',
            field=models.CharField(default=5, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloproductos',
            name='titulopost',
            field=models.CharField(default=4, max_length=250),
            preserve_default=False,
        ),
    ]