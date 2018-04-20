from __future__ import unicode_literals
from django.contrib import admin
from .models import Hero, ModuloImagen, ModuloCodigo, ModuloNoticia, ModuloProductos, Pagina, ModuloItem



class HeroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['descripcion']}),
        ('',             {'fields': ['boton']}),
        ('',             {'fields': ['color_del_boton']}),
        ('',             {'fields': ['URL']}),
        ('',             {'fields': ['imagen']}),

]


class ModuloImagenAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['subtitulo']}),
        ('',             {'fields': ['descripcion']}),
        ('',             {'fields': ['URL']}),
        ('',             {'fields': ['imagen']}),
        ('',             {'fields': ['nombre_del_URL']}),
]


class ModuloCodigoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',            {'fields': ['titulo']}),
        ('',            {'fields': ['subtitulo']}),
        ('',            {'fields': ['descripcion']}),
        ('',            {'fields': ['URL']}),
        ('',            {'fields': ['boton']}),
        ('',            {'fields': ['color_del_boton']}),
        ('',            {'fields': ['codigo']}),
]


class ModuloNoticiaAdmin(admin.ModelAdmin):
    fieldsets = [
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['subtitulo']}),
        ('',             {'fields': ['company']}),
        ('',             {'fields': ['imagen']}),
]

class ModuloItemTabularInLine(admin.TabularInline):
    model = ModuloItem
    fieldsets = [
        ('',     {'fields': ['imagen']}),
        ('',     {'fields': ['nombre_del_URL']}),
        ('',     {'fields': ['URL']}),
        ('',     {'fields': ['descripcion']}),
]


class ModuloProductosAdmin(admin.ModelAdmin):
    inlines = [ModuloItemTabularInLine]
    class Meta:
        model = ModuloProductos
    fieldsets = [
        ('',       {'fields': ['titulo']}),
        ('',       {'fields': ['subtitulo']}),    
]

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Titulo',          {'fields': ['titulo']}),
        ('Subtitulo',       {'fields': ['subtitulo']}),
        ('Descripcion',     {'fields': ['descripcion']}),
        ('Boton',           {'fields': ['boton']}),
]

admin.site.register(Hero, HeroAdmin)
admin.site.register(ModuloImagen, ModuloImagenAdmin)
admin.site.register(ModuloCodigo, ModuloCodigoAdmin)
admin.site.register(ModuloNoticia, ModuloNoticiaAdmin)
admin.site.register(ModuloProductos, ModuloProductosAdmin)
admin.site.register(Pagina, QuestionAdmin)
admin.site.register(ModuloItem)