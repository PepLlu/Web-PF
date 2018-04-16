from __future__ import unicode_literals
from django.contrib import admin
from .models import Pagina1, Pagina2, Pagina3, Pagina4, Pagina5, Pagina6

class ChoiceInline(admin.StackedInline):
    model = Pagina1
    extra = 3

class QuestionAdmin1(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',      {'fields': ['title']}),
        ('Descripcion', {'fields': ['desc']}),
        ('Boton',       {'fields': ['boton']}),
]

class ChoiceInline2(admin.StackedInline):
    model = Pagina2
    extra = 6

class QuestionAdmin2(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Link/Enlace',     {'fields': ['link']}),
]

class ChoiceInline3(admin.StackedInline):
    model = Pagina3
    extra = 4

class QuestionAdmin3(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',      {'fields': ['title']}),
        ('Subtitulo',   {'fields': ['subtitle']}),
        ('Descripcion', {'fields': ['desc']}),
        ('Boton',       {'fields': ['boton']}),
]

class ChoiceInline4(admin.StackedInline):
    model = Pagina4
    extra = 3

class QuestionAdmin4(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Company',         {'fields': ['company']}),
]

class ChoiceInline5(admin.StackedInline):
    model = Pagina5
    extra = 6

class QuestionAdmin5(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Link/Enlace',     {'fields': ['link']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Descripcion1',     {'fields': ['desc']}),
        ('Descripcion2',     {'fields': ['desc']}),
]

class ChoiceInline6(admin.StackedInline):
    model = Pagina6
    extra = 4

class QuestionAdmin6(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Boton',           {'fields': ['boton']}),
]

admin.site.register(Pagina1, QuestionAdmin1)
admin.site.register(Pagina2, QuestionAdmin2)
admin.site.register(Pagina3, QuestionAdmin3)
admin.site.register(Pagina4, QuestionAdmin4)
admin.site.register(Pagina5, QuestionAdmin5)
admin.site.register(Pagina6, QuestionAdmin6)
