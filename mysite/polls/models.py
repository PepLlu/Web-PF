# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Hero(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
    URL = models.URLField(max_length=200)
    color_del_boton = models.CharField(max_length=20)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Hero')
        verbose_name_plural = ('Hero cabezera')

    def __unicode__(self):
        return self.titulopost


class ModuloImagen(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    URL = models.URLField(max_length=200)
    nombre_del_URL = models.CharField(max_length=100)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Imagen')
        verbose_name_plural = ('Imagenes')

    def __unicode__(self):
        return self.titulopost



class ModuloCodigo(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)
    color_del_boton = models.CharField(max_length=20)
    codigo = models.TextField(max_length=500)
    URL = models.URLField(max_length=200)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Codigo')
        verbose_name_plural = ('Codigos')

    def __unicode__(self):
        return self.titulopost

class ModuloNoticia(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=50)
    company = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Noticia')
        verbose_name_plural = ('Noticias de la página')

    def __unicode__(self):
        return self.titulopost


class ModuloProductos(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __unicode__(self):
        return self.titulopost


class ModuloItem(models.Model):
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    nombre_del_URL = models.CharField(max_length=100)
    URL = models.URLField(max_length=200)
    descripcion = models.TextField(max_length=500)
    moduloproductos = models.ForeignKey(ModuloProductos)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Item de Producto')
        verbose_name_plural = ('Items de Productos')

    def __unicode__(self):
        return self.titulopost



class ModuloPrecios(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Precio')
        verbose_name_plural = ('Precios')

    def __unicode__(self):
        return self.titulopost


class ModuloItem2(models.Model):
    titulo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100)
    descripcion = models.TextField(max_length=40)
    descripcion1 = models.TextField(max_length=40)
    descripcion2 = models.TextField(max_length=40)
    boton = models.CharField(max_length=20)
    color_del_boton = models.CharField(max_length=20)
    URL = models.URLField(max_length=200)
    moduloprecios = models.ForeignKey(ModuloPrecios)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)    
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Item de Precio')
        verbose_name_plural = ('Items de Precios')

    def __unicode__(self):
        return self.titulopost


class ModuloPie(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=1000)
    URL = models.URLField(max_length=300)
    nombre_del_URL = models.CharField(max_length=100)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250)
    class Meta:
        verbose_name = ('Pie')
        verbose_name_plural = ('Pie de la página')

    def __unicode__(self):
        return self.titulopost


class Lesson(models.Model):
    titulopost = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    descripcion = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)        
    actualizado = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=10)


    def __str__(self):
        return self.titulo