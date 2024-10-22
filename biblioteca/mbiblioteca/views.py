from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuarios, Libros, Editorial, Autor
from .forms import UsuariosForm, AutorForm, LibrosForm, EditorialForm  

def inicio(request):
    return render(request, 'inicio.html', {})

# USUARIOS
def usuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, 'usuarios.html', {'usuarios': usuarios})

def usuariosadd(request):
    if request.method == 'POST':
        form = UsuariosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')  # URL 'usuarios' en urls.py
    else:
        form = UsuariosForm()
    return render(request, 'usuariosadd.html', {'form': form})

def usuariosupdate(request, usuarios_id):
    usuario = get_object_or_404(Usuarios, id=usuarios_id)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuariosForm(instance=usuario)
    return render(request, 'usuariosupdate.html', {'form': form, 'usuario': usuario})

def usuariosdel(request, usuarios_id):
    usuario = get_object_or_404(Usuarios, id=usuarios_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuarios')
    return render(request, 'usuariosdel.html', {'usuario': usuario})

# AUTOR
def autores(request):
    autores = Autor.objects.all()
    return render(request, 'autores.html', {'autores': autores})

def autoresadd(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('autores')  # URL 'autores' en urls.py
    else:
        form = AutorForm()
    return render(request, 'autoresadd.html', {'form': form})

##EDITAR, UPDATEAR Y ELIMINAR

def autoresupdate(request,autores_id):
    autores= get_object_or_404(Autor,id=autores_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autores)
        if form.is_valid():
            form.save()
            return redirect('autores')
    else:
        form = AutorForm(instance=autores)
    return render(request, 'autores.html', {'form': form})

def autoresdel(request,autores_id):
    autores= get_object_or_404(Autor,id=autores_id)
    if request.method == 'POST':
        autores.delete()
        return redirect('autores')
    return render(request, 'autoresdel.html', {'autores': autores})


# LIBROS
def libros(request):
    libros = Libros.objects.all()
    return render(request, 'libros.html', {'libros': libros})

def librosadd(request):
    if request.method == 'POST':
        form = LibrosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libros')  #  URL 'libros'  en  urls.py
    else:
        form = LibrosForm()
    return render(request, 'librosadd.html', {'form': form})

##EDITAR, UPDATEAR Y ELIMINAR

def librosupdate(request, libros_id):
    libro = get_object_or_404(Libros, id=libros_id)
    if request.method == 'POST':
        form = LibrosForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            return redirect('libros')  
    else:
        form = LibrosForm(instance=libro)
    return render(request, 'librosupdate.html', {'form': form, 'libros': libro})

def librosdel(request,libros_id):
    libros= get_object_or_404(libros,id=libros_id)
    if request.method == 'POST':
        libros.delete()
        return redirect('libros')
    return render(request, 'librosdel.html', {'libros': libros})

from django.shortcuts import render, redirect, get_object_or_404
from .models import Editorial  # Ensure this is imported
from .forms import EditorialForm  # Ensure you have this form imported


def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})


def editorialesadd(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editoriales')  # Redirect to the list of editorials after saving
    else:
        form = EditorialForm()
    return render(request, 'editorialesadd.html', {'form': form})


def editorialesupdate(request, editoriales_id):
    editorial = get_object_or_404(Editorial, id=editoriales_id)  # Correctly reference the model
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('editoriales')  # Redirect after saving
    else:
        form = EditorialForm(instance=editorial)
    return render(request, 'editorialesupdate.html', {'form': form, 'editorial': editorial})


def editorialesdel(request, editoriales_id):
    editorial = get_object_or_404(Editorial, id=editoriales_id)  # Correctly reference the model
    if request.method == 'POST':
        editorial.delete()  # Delete the editorial instance
        return redirect('editoriales')  # Redirect to the list of editorials after deletion
    return render(request, 'editorialesdel.html', {'editorial': editorial})