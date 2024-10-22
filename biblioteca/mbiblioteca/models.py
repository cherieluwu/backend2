from django.db import models
from django.utils import timezone
from mbiblioteca.choices import sexos, idioma


# Create your models here.
#USUARIOS

class Usuarios(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    nombre = models.CharField(max_length=99, verbose_name='Nombre')
    correo = models.EmailField(max_length=99, unique=True, verbose_name='Correo')
    password = models.CharField(max_length=99, verbose_name='Contraseña')
    created = models.DateField(default=timezone.now, verbose_name='Fecha de Creación')
    updated = models.DateField(auto_now=True, verbose_name='Fecha de Actualización')
    estado = models.IntegerField(default=1, blank=True)  # Estado por defecto

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

#AUTOR
class Autor(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    nombre = models.CharField(max_length=99, verbose_name='Nombre')
    biografia = models.TextField(verbose_name='Biografía')
    fnacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
    nacionalidad = models.TextField(max_length=99, verbose_name='Nacionalidad')
    estado = models.IntegerField(default=1)  # Estado por defecto

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "autor"
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


#EDITORIAL
class Editorial(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.IntegerField(default=1, verbose_name='Estado', blank=True)
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "editorial"
        verbose_name = "Editorial"
        verbose_name_plural = "Editoriales"
    
class Libros(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    titulo = models.CharField(max_length=200)
    id_autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Autor')
    fpublicacion = models.DateField(verbose_name='Fecha de Publicación')
    id_editorial = models.ForeignKey('Editorial', on_delete=models.CASCADE, default=1)  
    stock = models.IntegerField(verbose_name='Stock')
    nro_paginas = models.IntegerField(verbose_name='Número de Páginas')
    idioma = models.CharField(max_length=20, choices=[
        ('0', 'Español'),
        ('1', 'Inglés'),
        ('2', 'Portugués'),
    ], verbose_name='Idioma')  
    estado = models.IntegerField(default=1, blank=True)

    def __str__(self):
        return self.titulo

    class Meta:
        db_table = "libros"
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
        
#ROL
class Rol(models.Model):
    id = models.IntegerField(verbose_name='id', primary_key=True)
    estado = models.IntegerField(default=1, blank=True)  
    nombre = models.CharField(max_length=255, default='Default Name')
    def __str__(self):
        return self.nombre

    class Meta:
        db_table = "roles"
        verbose_name = "Rol"
        verbose_name_plural = "Roles"

        