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
    path('editorialesupdate/<int:editoriales_id>/', views.editorialesupdate, name='editorialesupdate'),   
    path('usuariosdel/<int:usuarios_id>/', views.usuariosdel, name='usuariosdel'),  # delete
    path('autoresupdate/<int:autores_id>/', views.autoresupdate, name='autoresupdate'),  # update
    path('usuariosupdate/<int:usuarios_id>/', views.usuariosupdate, name='usuariosupdate'),
    path('autoresdel/<int:autores_id>/', views.autoresdel, name='autoresdel'),  # delete
    path('librosupdate/<int:libros_id>/', views.librosupdate, name='librosupdate'),  # update
    path('librosedel/<int:libros_id>/', views.librosdel, name='librosdel'),
    path('editorialesupdate/<int:editoriales_id>/', views.editorialesupdate, name='editorialesupdate'),  # update
    path('editorialesdel/<int:editoriales_id>/', views.editorialesdel, name='editorialesdel'),  # delete
]