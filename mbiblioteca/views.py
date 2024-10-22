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

def usuariosedit(request, usuarios_id):
    usuario = get_object_or_404(Usuarios, pk=usuarios_id)
    form = UsuariosForm(instance=usuario)
    return render(request, 'usuarios.html', {'form': form})

def usuariosupdate(request,usuario_id):
    usuario= get_object_or_404(Usuarios,id=usuario_id)
    if request.method == 'POST':
        form = UsuariosForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
        else:
            form = UsuariosForm(instance=usuario)
            return render(request, 'usuarios.html', {'form': form})

def usuariosdel(request, usuario_id):
    usuario = get_object_or_404(Usuarios, id=usuario_id)
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
def autoresedit(request,autores_id):
    autores= get_object_or_404(Autor,id=autores_id)
    form=AutorForm(instance=autores)
    return render(request, 'autoresedit.html', {'form': form,'autores':autores})

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
def librosedit(request,libros_id):
    libros= get_object_or_404(libros,id=libros_id)
    form=LibrosForm(instance=libros)
    return render(request, 'librosedit.html', {'form': form,'libros':libros})

def librosupdate(request,libros_id):
    libros= get_object_or_404(libros,id=libros_id)
    if request.method == 'POST':
        form = LibrosForm(request.POST, instance=libros)
        if form.is_valid():
            form.save()
            return redirect('libros')
        else:
            form = LibrosForm(instance=libros)
            return render(request, 'libros.html', {'form': form})

def librosdel(request,libros_id):
    libros= get_object_or_404(libros,id=libros_id)
    if request.method == 'POST':
        libros.delete()
        return redirect('libros')
    return render(request, 'librosdel.html', {'libros': libros})

# EDITORIALES
def editoriales(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editoriales.html', {'editoriales': editoriales})

def editorialesadd(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editoriales')  #URL 'editoriales' en  urls.py
    else:
        form = EditorialForm()
    return render(request, 'editorialesadd.html', {'form': form})

##EDITAR, UPDATEAR Y ELIMINAR
def editorialesedit(request, editoriales_id):
    editorial = get_object_or_404(Editorial, id=editoriales_id)
    form = EditorialForm(instance=editorial)

    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('editoriales')  

    context = {'form': form, 'editorial': editorial}
    return render(request, 'editorialesedit.html', context)

def editorialesupdate(request,editoriales_id):
    editorial= get_object_or_404(editorial,id=editoriales_id)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            return redirect('editoriales')
        else:
            form = EditorialForm(instance=editorial)
    return render(request, 'editoriales.html', {'form': form})

def editorialesdel(request,editoriales_id):
    editoriales= get_object_or_404(editoriales,id=editoriales_id)
    if request.method == 'POST':
        editoriales.delete()
        return redirect('editoriales')
    return render(request, 'editorialesdel.html', {'editoriales': editoriales})