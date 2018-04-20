# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Hero(models.Model):
    verbose_name = 'Hero'
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
    URL = models.URLField(max_length=200)
    color_del_boton = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)

class ModuloImagen(models.Model):
    verbose_name = 'Imagen'
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    URL = models.URLField(max_length=200)
    nombre_del_URL = models.CharField(max_length=100)

class ModuloCodigo(models.Model):
    verbose_name = 'Codigo'
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
    color_del_boton = models.CharField(max_length=20)
    codigo = models.TextField(max_length=500)
    URL = models.URLField(max_length=200)

class ModuloNoticia(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=50)
    company = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)

class ModuloProductos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    
        
class ModuloItem(models.Model):
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    nombre_del_URL = models.CharField(max_length=100)
    URL = models.URLField(max_length=200)
    descripcion = models.TextField(max_length=500)
    moduloproductos = models.ForeignKey('ModuloProductos')

class Pagina(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
