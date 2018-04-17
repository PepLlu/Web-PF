# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Hero(models.Model):
    verbose_name = 'Hero'
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
    URL = models.URLField(max_length=200)
    color_bot = models.CharField(max_length=20)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)

class ModuloImagen(models.Model):
    verbose_name = 'Imagen'
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    img = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    link = models.URLField(max_length=200)

class Pagina3(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)

class Pagina4(models.Model):
    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=50)
    company = models.CharField(max_length=40)

class Pagina5(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    link = models.CharField(max_length=20)
    desc = models.TextField(max_length=500)

class Pagina6(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
