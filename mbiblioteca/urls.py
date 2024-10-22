from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('autores/', views.autores, name='autores'),
    path('autoresadd/', views.autoresadd, name='autoresadd'),
    path('libros/', views.libros, name='libros'),
    path('librosadd/', views.librosadd, name='librosadd'),
    path('usuarios/', views.usuarios, name='usuarios'),
    path('usuariosadd/', views.usuariosadd, name='usuariosadd'),
    path('editoriales/', views.editoriales, name='editoriales'),
    path('editorialesadd/', views.editorialesadd, name='editorialesadd'),
    path('usuariosupdate/<int:usuarios_id>/', views.usuariosupdate, name='usuariosupdate'),  # update
    path('usuariosdel/<int:usuarios_id>/', views.usuariosdel, name='usuariosdel'),  # delete
    path('usuariosedit/<int:usuarios_id>/', views.usuariosedit, name='usuariosedit'),
    path('autoresedit/<int:autores_id>/', views.autoresedit, name='autoresedit'),  # edit
    path('autoresupdate/<int:autores_id>/', views.autoresupdate, name='autoresupdate'),  # update
    path('autoresdel/<int:autores_id>/', views.autoresdel, name='autoresdel'),  # delete
    path('librosedit/<int:libros_id>/', views.librosedit, name='librosedit'),  # edit
    path('librosupdate/<int:libros_id>/', views.librosupdate, name='librosupdate'),  # update
    path('librosedel/<int:libros_id>/', views.librosdel, name='librosdel'),
    path('mbiblioteca/editorialesedit/<int:editoriales_id>/', views.editorialesedit, name='editorialesedit'),
    path('editorialesupdate/<int:editoriales_id>/', views.editorialesupdate, name='editorialesupdate'),  # update
    path('editorialesdel/<int:editoriales_id>/', views.editorialesdel, name='editorialesdel'),  # delete
]