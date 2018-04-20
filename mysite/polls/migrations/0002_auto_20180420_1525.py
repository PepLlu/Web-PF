# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-20 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModuloItem2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('imagen', models.ImageField(upload_to='img/%Y/%m/%d/')),
                ('descripcion', models.TextField(max_length=40)),
                ('descripcion1', models.TextField(max_length=40)),
                ('descripcion2', models.TextField(max_length=40)),
                ('boton', models.CharField(max_length=20)),
                ('color_del_boton', models.CharField(max_length=20)),
                ('URL', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ModuloPrecios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Pagina',
        ),
        migrations.AddField(
            model_name='moduloitem2',
            name='moduloprecios',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.ModuloPrecios'),
        ),
    ]