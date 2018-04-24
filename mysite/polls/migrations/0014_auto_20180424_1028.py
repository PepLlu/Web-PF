# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-24 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0013_auto_20180424_0932'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modulocodigo',
            name='codigo',
        ),
        migrations.AlterField(
            model_name='hero',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida para el Bot\xf3n.', verbose_name='URL del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='boton',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza en el Bot\xf3n.', max_length=20, verbose_name='Texto del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='color_del_boton',
            field=models.CharField(help_text='Introduzca el color del Bot\xf3n (Black, White, Green...).', max_length=20, verbose_name='Color del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 1000 car\xe1cteres.', max_length=1000, verbose_name='Descripci\xf3n de la Noticia'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='imagen',
            field=models.ImageField(help_text='Introduzca una imag\xe9n para el fondo de pantalla.', upload_to='img/%Y/%m/%d/', verbose_name='Fondo de pantalla / Background'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo de la Noticia.', max_length=100, verbose_name='Titulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='hero',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida para el Bot\xf3n.', verbose_name='URL del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='boton',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza en el Bot\xf3n.', max_length=20, verbose_name='Texto del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='color_del_boton',
            field=models.CharField(help_text='Introduzca el color del Bot\xf3n (Black, White, Green...).', max_length=20, verbose_name='Color del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 1000 car\xe1cteres.', max_length=1000, verbose_name='Descripci\xf3n de la Noticia'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='subtitulo',
            field=models.CharField(help_text='Introduzca el subtitulo de la Noticia.', max_length=50, verbose_name='Subtitulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo de la Noticia.', max_length=100, verbose_name='Titulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='modulocodigo',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida.', verbose_name='URL de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 1000 car\xe1cteres.', max_length=1000, verbose_name='Descripci\xf3n de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='imagen',
            field=models.ImageField(help_text='Introduzca una imag\xe9n para que aparezca al lado de la Noticia.', upload_to='img/%Y/%m/%d/', verbose_name='Imag\xe9n de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='nombre_del_URL',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza enlazado.', max_length=100, verbose_name='Texto de la URL'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='subtitulo',
            field=models.CharField(help_text='Introduzca el subtitulo de la Noticia.', max_length=50, verbose_name='Subtitulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo de la Noticia.', max_length=100, verbose_name='Titulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloimagen',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='moduloitem',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida.', verbose_name='URL de la Noticia'),
        ),
        migrations.AlterField(
            model_name='moduloitem',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 50 car\xe1cteres.', max_length=50, verbose_name='Descripci\xf3n del producto'),
        ),
        migrations.AlterField(
            model_name='moduloitem',
            name='imagen',
            field=models.ImageField(help_text='Introduzca una imag\xe9n.', upload_to='img/%Y/%m/%d/', verbose_name='Imag\xe9n que prefieras.'),
        ),
        migrations.AlterField(
            model_name='moduloitem',
            name='nombre_del_URL',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza enlazado.', max_length=100, verbose_name='Texto de la URL'),
        ),
        migrations.AlterField(
            model_name='moduloitem',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida para el Bot\xf3n.', verbose_name='URL del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='boton',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza en el Bot\xf3n.', max_length=20, verbose_name='Texto del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='color_del_boton',
            field=models.CharField(help_text='Introduzca el color del Bot\xf3n (Black, White, Green...).', max_length=20, verbose_name='Color del Bot\xf3n'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 40 car\xe1cteres.', max_length=40, verbose_name='Descripci\xf3n 1 del producto'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='descripcion1',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 40 car\xe1cteres.', max_length=40, verbose_name='Descripci\xf3n 2 del producto'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='descripcion2',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 40 car\xe1cteres.', max_length=40, verbose_name='Descripci\xf3n 3 del producto'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='imagen',
            field=models.ImageField(help_text='Introduzca una imag\xe9n.', upload_to='img/%Y/%m/%d/', verbose_name='Imag\xe9n que prefieras.'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo del Producto', max_length=100, verbose_name='Titulo del Producto'),
        ),
        migrations.AlterField(
            model_name='moduloitem2',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='modulonoticia',
            name='company',
            field=models.CharField(help_text='Introduzca el nombre de la Compa\xf1ia o empresa.', max_length=40, verbose_name='Compa\xf1ia o empresa.'),
        ),
        migrations.AlterField(
            model_name='modulonoticia',
            name='imagen',
            field=models.ImageField(help_text='Introduzca una imag\xe9n para el fondo de pantalla.', upload_to='img/%Y/%m/%d/', verbose_name='Fondo de pantalla / Background'),
        ),
        migrations.AlterField(
            model_name='modulonoticia',
            name='subtitulo',
            field=models.CharField(help_text='Introduzca el subtitulo de la Noticia.', max_length=50, verbose_name='Subtitulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='modulonoticia',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo de la Noticia.', max_length=100, verbose_name='Titulo de la Noticia'),
        ),
        migrations.AlterField(
            model_name='modulonoticia',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='modulopie',
            name='URL',
            field=models.URLField(help_text='Introduzca una URL v\xe1lida.', verbose_name='URL v\xe1lida'),
        ),
        migrations.AlterField(
            model_name='modulopie',
            name='descripcion',
            field=models.TextField(help_text='Introduzca una descripci\xf3n, m\xe1ximo 1500 car\xe1cteres.', max_length=1500, verbose_name='Descripci\xf3n del Pie de P\xe1gina'),
        ),
        migrations.AlterField(
            model_name='modulopie',
            name='nombre_del_URL',
            field=models.CharField(help_text='Introduzca el texto que quieras para que apareza enlazado.', max_length=100, verbose_name='Texto de la URL'),
        ),
        migrations.AlterField(
            model_name='modulopie',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo del Pie de P\xe1gina.', max_length=100, verbose_name='Titulo del Pie de P\xe1gina'),
        ),
        migrations.AlterField(
            model_name='modulopie',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
        migrations.AlterField(
            model_name='moduloprecios',
            name='subtitulo',
            field=models.CharField(help_text='Introduzca el subtitulo de las Tarifas.', max_length=50, verbose_name='Subtitulo de las Tarifas'),
        ),
        migrations.AlterField(
            model_name='moduloprecios',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo de las Tarifas.', max_length=100, verbose_name='Titulo de las Tarifas'),
        ),
        migrations.AlterField(
            model_name='moduloproductos',
            name='subtitulo',
            field=models.CharField(help_text='Introduzca el subtitulo del Producto.', max_length=50, verbose_name='Subtitulo del Producto'),
        ),
        migrations.AlterField(
            model_name='moduloproductos',
            name='titulo',
            field=models.CharField(help_text='Introduzca el titulo del Producto', max_length=100, verbose_name='Titulo del Producto'),
        ),
        migrations.AlterField(
            model_name='moduloproductos',
            name='titulopost',
            field=models.CharField(help_text='Introduzca el titulo del Post', max_length=250, verbose_name='Titulo Post'),
        ),
    ]
