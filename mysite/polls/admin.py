from __future__ import unicode_literals
from django.contrib import admin
from .models import Hero, ModuloImagen, ModuloCodigo, ModuloNoticia, ModuloProductos, ModuloPrecios, ModuloItem, ModuloItem2, ModuloPie, Lesson



class HeroAdmin(admin.ModelAdmin):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['descripcion']}),
        ('',             {'fields': ['boton']}),
        ('',             {'fields': ['color_del_boton']}),
        ('',             {'fields': ['URL']}),
        ('',             {'fields': ['imagen']}),

]


class ModuloImagenAdmin(admin.ModelAdmin):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['subtitulo']}),
        ('',             {'fields': ['descripcion']}),
        ('',             {'fields': ['URL']}),
        ('',             {'fields': ['imagen']}),
        ('',             {'fields': ['nombre_del_URL']}),
]


class ModuloCodigoAdmin(admin.ModelAdmin):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',            {'fields': ['titulo']}),
        ('',            {'fields': ['subtitulo']}),
        ('',            {'fields': ['descripcion']}),
        ('',            {'fields': ['URL']}),
        ('',            {'fields': ['boton']}),
        ('',            {'fields': ['color_del_boton']}),
        ('',            {'fields': ['codigo']}),
]


class ModuloNoticiaAdmin(admin.ModelAdmin):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',             {'fields': ['titulo']}),
        ('',             {'fields': ['subtitulo']}),
        ('',             {'fields': ['company']}),
        ('',             {'fields': ['imagen']}),
]

class ModuloItemStackedInline(admin.StackedInline):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    model = ModuloItem
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',     {'fields': ['imagen']}),
        ('',     {'fields': ['nombre_del_URL']}),
        ('',     {'fields': ['URL']}),
        ('',     {'fields': ['descripcion']}),
]


class ModuloProductosAdmin(admin.ModelAdmin):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    inlines = [ModuloItemStackedInline]
    class Meta:
        model = ModuloProductos
    fieldsets = [
        ('',       {'fields': ['titulopost']}),
        ('',       {'fields': ['titulo']}),
        ('',       {'fields': ['subtitulo']}),    
]

class ModuloItem2StackedInline(admin.StackedInline):
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    model = ModuloItem2
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
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
    search_fields = ('titulopost', 'descripcion')
    list_filter = ('creado', 'actualizado', 'estado')
    inlines = [ModuloItem2StackedInline]
    class Meta:
        model = ModuloPrecios
    fieldsets = [
        ('',             {'fields': ['titulopost']}),
        ('',       {'fields': ['titulo']}),
        ('',       {'fields': ['subtitulo']}),
    ]


class ModuloPieAdmin(admin.ModelAdmin):
        search_fields = ('titulopost', 'descripcion')
        list_filter = ('creado', 'actualizado', 'estado')
        ('',            {'fields': ['titulopost']}),
        ('',            {'fields': ['titulo']})
        ('',            {'fields': ['descripcion']})
        ('',            {'fields': ['URL']})
        ('',            {'fields': ['nombre_del_URL']})

class LessonAdmin(admin.ModelAdmin):
        list_display = ('titulopost', 'slug', 'creado', 'estado')
        list_filter = ('creado', 'actualizado', 'estado')
        search_fields = ('titulopost', 'descripcion')

admin.site.register(Hero, HeroAdmin)
admin.site.register(ModuloImagen, ModuloImagenAdmin)
admin.site.register(ModuloCodigo, ModuloCodigoAdmin)
admin.site.register(ModuloNoticia, ModuloNoticiaAdmin)
admin.site.register(ModuloProductos, ModuloProductosAdmin)
admin.site.register(ModuloPrecios, ModuloPreciosAdmin)
admin.site.register(ModuloItem)
admin.site.register(ModuloPie, ModuloPieAdmin)
admin.site.register(Lesson, LessonAdmin)
