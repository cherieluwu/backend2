# Generated by Django 5.1.1 on 2024-10-22 02:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mbiblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('titulo', models.CharField(max_length=200)),
                ('fpublicacion', models.DateField(verbose_name='Fecha de Publicación')),
                ('stock', models.IntegerField(verbose_name='Stock')),
                ('nro_paginas', models.IntegerField(verbose_name='Número de Páginas')),
                ('idioma', models.IntegerField(verbose_name='Idioma')),
                ('estado', models.IntegerField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'db_table': 'libros',
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=99, verbose_name='Nombre')),
                ('correo', models.EmailField(max_length=99, unique=True, verbose_name='Correo')),
                ('password', models.CharField(max_length=99, verbose_name='Contraseña')),
                ('created', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha de Creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de Actualización')),
                ('estado', models.IntegerField(blank=True, default=1)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'usuarios',
            },
        ),
        migrations.RemoveField(
            model_name='libro',
            name='autor',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.RemoveField(
            model_name='editorial',
            name='creado',
        ),
        migrations.AlterField(
            model_name='autor',
            name='estado',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='estado',
            field=models.IntegerField(blank=True, default=1, verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='rol',
            name='estado',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='rol',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, verbose_name='id'),
        ),
        migrations.AlterField(
            model_name='rol',
            name='nombre',
            field=models.CharField(default='Default Name', max_length=255),
        ),
        migrations.AddField(
            model_name='libros',
            name='autor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.autor', verbose_name='Autor'),
        ),
        migrations.AddField(
            model_name='libros',
            name='id_editorial',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mbiblioteca.editorial'),
        ),
        migrations.DeleteModel(
            name='Libro',
        ),
    ]