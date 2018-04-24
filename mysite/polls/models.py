# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class Hero(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo de la Noticia', 
    help_text = 'Introduzca el titulo de la Noticia.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=1000,
    verbose_name = 'Descripción de la Noticia', 
    help_text = 'Introduzca una descripción, máximo 1000 carácteres.'
    )
    boton = models.CharField(max_length=20,
    verbose_name = 'Texto del Botón', 
    help_text = 'Introduzca el texto que quieras para que apareza en el Botón.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL del Botón', 
    help_text = 'Introduzca una URL válida para el Botón.'
    )
    color_del_boton = models.CharField(max_length=20,
    verbose_name = 'Color del Botón', 
    help_text = 'Introduzca el color del Botón (Black, White, Green...).'
    )
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,
    verbose_name = 'Fondo de pantalla / Background', 
    help_text = 'Introduzca una imagén para el fondo de pantalla.'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Hero')
        verbose_name_plural = ('Hero cabezera')

    def __unicode__(self):
        return self.titulopost


class ModuloImagen(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo de la Noticia', 
    help_text = 'Introduzca el titulo de la Noticia.'
    )
    subtitulo = models.CharField(max_length=50,
    verbose_name = 'Subtitulo de la Noticia', 
    help_text = 'Introduzca el subtitulo de la Noticia.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=1000,
    verbose_name = 'Descripción de la Noticia', 
    help_text = 'Introduzca una descripción, máximo 1000 carácteres.'
    )
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,
    verbose_name = 'Imagén de la Noticia', 
    help_text = 'Introduzca una imagén para que aparezca al lado de la Noticia.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL de la Noticia', 
    help_text = 'Introduzca una URL válida.'
    )
    nombre_del_URL = models.CharField(max_length=100,
    verbose_name = 'Texto de la URL', 
    help_text = 'Introduzca el texto que quieras para que apareza enlazado.'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Imagen')
        verbose_name_plural = ('Imagenes')

    def __unicode__(self):
        return self.titulopost



class ModuloCodigo(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo de la Noticia', 
    help_text = 'Introduzca el titulo de la Noticia.'
    )
    subtitulo = models.CharField(max_length=50,
    verbose_name = 'Subtitulo de la Noticia', 
    help_text = 'Introduzca el subtitulo de la Noticia.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=1000,
    verbose_name = 'Descripción de la Noticia', 
    help_text = 'Introduzca una descripción, máximo 1000 carácteres.'
    )
    boton = models.CharField(max_length=20,
    verbose_name = 'Texto del Botón', 
    help_text = 'Introduzca el texto que quieras para que apareza en el Botón.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL del Botón', 
    help_text = 'Introduzca una URL válida para el Botón.'
    )
    color_del_boton = models.CharField(max_length=20,
    verbose_name = 'Color del Botón', 
    help_text = 'Introduzca el color del Botón (Black, White, Green...).'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Codigo')
        verbose_name_plural = ('Codigos')

    def __unicode__(self):
        return self.titulopost

class ModuloNoticia(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo de la Noticia', 
    help_text = 'Introduzca el titulo de la Noticia.'
    )
    subtitulo = models.CharField(max_length=50,
    verbose_name = 'Subtitulo de la Noticia', 
    help_text = 'Introduzca el subtitulo de la Noticia.'
    )
    company = models.CharField(max_length=40,
    verbose_name = 'Compañia o empresa.', 
    help_text = 'Introduzca el nombre de la Compañia o empresa.'
    )
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,
    verbose_name = 'Fondo de pantalla / Background', 
    help_text = 'Introduzca una imagén para el fondo de pantalla.'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Noticia')
        verbose_name_plural = ('Noticias de la página')

    def __unicode__(self):
        return self.titulopost


class ModuloProductos(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo del Producto', 
    help_text = 'Introduzca el titulo del Producto'
    )
    subtitulo = models.CharField(max_length=50,
    verbose_name = 'Subtitulo del Producto', 
    help_text = 'Introduzca el subtitulo del Producto.'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Producto')
        verbose_name_plural = ('Productos')

    def __unicode__(self):
        return self.titulopost


class ModuloItem(models.Model):
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,
    verbose_name = 'Imagén que prefieras.', 
    help_text = 'Introduzca una imagén.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL de la Noticia', 
    help_text = 'Introduzca una URL válida.'
    )
    nombre_del_URL = models.CharField(max_length=100,
    verbose_name = 'Texto de la URL', 
    help_text = 'Introduzca el texto que quieras para que apareza enlazado.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=50,
    verbose_name = 'Descripción del producto', 
    help_text = 'Introduzca una descripción, máximo 50 carácteres.'
    )
    moduloproductos = models.ForeignKey(ModuloProductos)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Item de Producto')
        verbose_name_plural = ('Items de Productos')

    def __unicode__(self):
        return self.titulopost



class ModuloPrecios(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo de las Tarifas', 
    help_text = 'Introduzca el titulo de las Tarifas.'
    )
    subtitulo = models.CharField(max_length=50,
    verbose_name = 'Subtitulo de las Tarifas', 
    help_text = 'Introduzca el subtitulo de las Tarifas.'
    )
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
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo del Producto', 
    help_text = 'Introduzca el titulo del Producto'
    )
    imagen = models.ImageField(upload_to='img/%Y/%m/%d/', height_field=None, width_field=None, max_length=100,
    verbose_name = 'Imagén que prefieras.', 
    help_text = 'Introduzca una imagén.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=40,
    verbose_name = 'Descripción 1 del producto', 
    help_text = 'Introduzca una descripción, máximo 40 carácteres.'
    )
    descripcion1 = RichTextUploadingField(config_name='full', max_length=40,
    verbose_name = 'Descripción 2 del producto', 
    help_text = 'Introduzca una descripción, máximo 40 carácteres.'
    )
    descripcion2 = RichTextUploadingField(config_name='full', max_length=40,
    verbose_name = 'Descripción 3 del producto', 
    help_text = 'Introduzca una descripción, máximo 40 carácteres.'
    )
    boton = models.CharField(max_length=20,
    verbose_name = 'Texto del Botón', 
    help_text = 'Introduzca el texto que quieras para que apareza en el Botón.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL del Botón', 
    help_text = 'Introduzca una URL válida para el Botón.'
    )
    color_del_boton = models.CharField(max_length=20,
    verbose_name = 'Color del Botón', 
    help_text = 'Introduzca el color del Botón (Black, White, Green...).'
    )
    moduloprecios = models.ForeignKey(ModuloPrecios)
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)    
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
    class Meta:
        verbose_name = ('Item de Precio')
        verbose_name_plural = ('Items de Precios')

    def __unicode__(self):
        return self.titulopost


class ModuloPie(models.Model):
    titulo = models.CharField(max_length=100,
    verbose_name = 'Titulo del Pie de Página', 
    help_text = 'Introduzca el titulo del Pie de Página.'
    )
    descripcion = RichTextUploadingField(config_name='full', max_length=1500,
    verbose_name = 'Descripción del Pie de Página', 
    help_text = 'Introduzca una descripción, máximo 1500 carácteres.'
    )
    URL = models.URLField(max_length=200,
    verbose_name = 'URL válida', 
    help_text = 'Introduzca una URL válida.'
    )
    nombre_del_URL = models.CharField(max_length=100,
    verbose_name = 'Texto de la URL', 
    help_text = 'Introduzca el texto que quieras para que apareza enlazado.'
    )
    creado = models.DateTimeField(null=True, blank=True, auto_now_add=True)        
    actualizado = models.DateTimeField(null=True, blank=True, auto_now=True)
    estado = models.CharField(null=True, blank=True, max_length=10)
    titulopost = models.CharField(max_length=250, 
    verbose_name = 'Titulo Post', 
    help_text = 'Introduzca el titulo del Post'
    )
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