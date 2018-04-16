# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib import admin

class Pagina1(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    boton = models.CharField(max_length=20)

class Pagina2(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)
    link = models.CharField(max_length=20)

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
