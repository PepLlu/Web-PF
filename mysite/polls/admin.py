from __future__ import unicode_literals
from django.contrib import admin
from .models import Hero, ModuloImagen, ModuloCodigo, ModuloNoticia, ModuloProductos, ModuloPrecios, ModuloItem, ModuloItem2



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

class ModuloItemStackedInline(admin.StackedInline):
    model = ModuloItem
    fieldsets = [
        ('',     {'fields': ['imagen']}),
        ('',     {'fields': ['nombre_del_URL']}),
        ('',     {'fields': ['URL']}),
        ('',     {'fields': ['descripcion']}),
]


class ModuloProductosAdmin(admin.ModelAdmin):
    inlines = [ModuloItemStackedInline]
    class Meta:
        model = ModuloProductos
    fieldsets = [
        ('',       {'fields': ['titulo']}),
        ('',       {'fields': ['subtitulo']}),    
]

class ModuloItem2StackedInline(admin.StackedInline):
    model = ModuloItem2
    fieldsets = [
        ('',            {'fields': ['titulo']}),
        ('',            {'fields': ['imagen']}),
        ('',            {'fields': ['descripcion']}),
        ('',            {'fields': ['descripcion1']}),
        ('',            {'fields': ['descripcion2']}),
        ('',            {'fields': ['boton']}),
        ('',            {'fields': ['color_del_boton']}),
        ('',            {'fields': ['URL']}),


]


class ModuloPreciosAdmin(admin.ModelAdmin):
    inlines = [ModuloItem2StackedInline]
    class Meta:
        model = ModuloPrecios
    fieldsets = [
        ('',       {'fields': ['titulo']}),
        ('',       {'fields': ['subtitulo']}),
    ]
    
admin.site.register(Hero, HeroAdmin)
admin.site.register(ModuloImagen, ModuloImagenAdmin)
admin.site.register(ModuloCodigo, ModuloCodigoAdmin)
admin.site.register(ModuloNoticia, ModuloNoticiaAdmin)
admin.site.register(ModuloProductos, ModuloProductosAdmin)
admin.site.register(ModuloPrecios, ModuloPreciosAdmin)
admin.site.register(ModuloItem)