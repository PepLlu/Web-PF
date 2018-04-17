from __future__ import unicode_literals
from django.contrib import admin
from .models import Hero, Cabezera, Pagina3, Pagina4, Pagina5, Pagina6


class HeroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Boton',           {'fields': ['boton']}),
        ('Color del Boton', {'fields': ['color_bot']}),
        ('URL',             {'fields': ['URL']}),
        ('Imagen',          {'fields': ['img']}),
]


class QuestionAdmin2(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Link/Enlace',     {'fields': ['link']}),
]


class QuestionAdmin3(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',      {'fields': ['title']}),
        ('Subtitulo',   {'fields': ['subtitle']}),
        ('Descripcion', {'fields': ['desc']}),
        ('Boton',       {'fields': ['boton']}),
]


class QuestionAdmin4(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Company',         {'fields': ['company']}),
]


class QuestionAdmin5(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Link/Enlace',     {'fields': ['link']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Descripcion1',     {'fields': ['desc']}),
        ('Descripcion2',     {'fields': ['desc']}),
]


class QuestionAdmin6(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['title']}),
        ('Subtitulo',       {'fields': ['subtitle']}),
        ('Descripcion',     {'fields': ['desc']}),
        ('Boton',           {'fields': ['boton']}),
]

admin.site.register(Hero, HeroAdmin)
admin.site.register(Cabezera, QuestionAdmin2)
admin.site.register(Pagina3, QuestionAdmin3)
admin.site.register(Pagina4, QuestionAdmin4)
admin.site.register(Pagina5, QuestionAdmin5)
admin.site.register(Pagina6, QuestionAdmin6)
