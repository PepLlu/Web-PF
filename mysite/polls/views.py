# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Hero, ModuloImagen, ModuloCodigo, ModuloNoticia, ModuloProductos, Pagina, ModuloItem

def index(request):
    hero = Hero.objects.first()
    moduloimagen = ModuloImagen.objects.first()
    modulocodigo = ModuloCodigo.objects.first()
    modulonoticia = ModuloNoticia.objects.first()
    moduloproductos = ModuloProductos.objects.first()
    moduloitems = ModuloItem.objects.all()
    pagina = Pagina.objects.first()

    return render(request, 'inde/index.html', {
        'hero': hero,
        'moduloimagen': moduloimagen,
        'modulocodigo': modulocodigo,
        'modulonoticia': modulonoticia,
        'moduloproductos': moduloproductos,
        'pagina': pagina,
        'moduloitems': moduloitems,
        })

def pagina(request):
    return render(request, 'polls/pagina.html', {})

    
    