# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 13:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20180420_1525'),
    ]

    operations = [
        migrations.AddField(
            model_name='moduloprecios',
            name='subtitulo',
            field=models.CharField(default='eo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moduloprecios',
            name='titulo',
            field=models.CharField(default='titulo', max_length=100),
            preserve_default=False,
        ),
    ]
