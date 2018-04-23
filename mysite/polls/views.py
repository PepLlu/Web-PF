# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Hero, ModuloImagen, ModuloCodigo, ModuloNoticia, ModuloProductos, ModuloItem2, ModuloItem, ModuloPrecios, ModuloPie

def index(request):
    hero = Hero.objects.first()
    moduloimagen = ModuloImagen.objects.first()
    modulocodigo = ModuloCodigo.objects.first()
    modulonoticia = ModuloNoticia.objects.first()
    moduloproductos = ModuloProductos.objects.first()
    moduloitems = ModuloItem.objects.all()
    moduloprecios = ModuloPrecios.objects.first()
    moduloitems2 = ModuloItem2.objects.all()
    modulopie = ModuloPie.objects.first()

    return render(request, 'inde/index.html', {
        'hero': hero,
        'moduloimagen': moduloimagen,
        'modulocodigo': modulocodigo,
        'modulonoticia': modulonoticia,
        'moduloproductos': moduloproductos,
        'moduloprecios': moduloprecios,
        'moduloitems': moduloitems,
        'moduloitems2': moduloitems2,
        'modulopie': modulopie,
        })

def pagina(request):
    return render(request, 'polls/pagina.html', {})

    
    