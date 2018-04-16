# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Pagina1, Pagina2, Pagina3, Pagina4, Pagina5, Pagina6

def index(request):
    pagina1 = Pagina1.objects.first()
    pagina2 = Pagina2.objects.first()
    pagina3 = Pagina3.objects.first()
    pagina4 = Pagina4.objects.first()
    pagina5 = Pagina5.objects.first()
    pagina6 = Pagina6.objects.first()
    return render(request, 'inde/index.html', {
        'pagina1': pagina1,
        'pagina2': pagina2,
        'pagina3': pagina3,
        'pagina4': pagina4,
        'pagina5': pagina5,
        'pagina6': pagina6,})

def pagina(request):
    return render(request, 'polls/pagina.html', {})
