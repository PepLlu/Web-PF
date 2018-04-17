# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-17 07:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0007_auto_20180416_1557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.TextField(max_length=500)),
                ('boton', models.CharField(max_length=20)),
                ('URL', models.URLField()),
                ('color_bot', models.CharField(max_length=20)),
                ('img', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.DeleteModel(
            name='Portada',
        ),
    ]
