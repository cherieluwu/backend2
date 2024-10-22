from django.contrib import admin
from mbiblioteca.models import Usuarios, Editorial, Libros, Autor, Rol

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'correo', 'estado', 'created', 'updated']

class AutorAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'biografia', 'fnacimiento', 'nacionalidad', 'estado']

class LibroAdmin(admin.ModelAdmin):
    list_display = ['id', 'titulo', 'id_autor', 'fpublicacion', 'id_editorial', 'stock', 'nro_paginas', 'idioma', 'estado']

class EditorialAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'estado']

class RolAdmin(admin.ModelAdmin):
    list_display = ['id', 'estado']

# Registrando los modelos en el admin
admin.site.register(Usuarios, UsuarioAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libros, LibroAdmin)
admin.site.register(Editorial, EditorialAdmin)
admin.site.register(Rol, RolAdmin)