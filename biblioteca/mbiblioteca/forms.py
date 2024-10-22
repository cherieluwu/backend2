from django import forms
from mbiblioteca.choices import idioma 
from .models import Usuarios, Editorial, Libros, Autor, Rol
import datetime

# USUARIOS
class UsuariosForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NOMBRE'}))
    correo = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CORREO ELECTRONICO'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'PASSWORD'}))  
    created = forms.DateField(widget=forms.SelectDateWidget(years=range(1800, 2034), attrs={'class': 'form-control', 'placeholder': 'FECHA DE CREACIÓN'}))  
    id_rol = forms.IntegerField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'ROL (0=ALUMNO, 1=DOCENTE, 2=BIBLIOTECARIO)'}),label='ID Rol')
    updated = forms.DateField(widget=forms.SelectDateWidget(years=range(1800, 2034), attrs={'class': 'form-control', 'placeholder': 'FECHA DE ACTUALIZACIÓN'}))
    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ESTADO'}), required=False)

    class Meta:
        model = Usuarios
        fields = '__all__'

# EDITORIAL
class EditorialForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NOMBRE EDITORIAL'}))
    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ESTADO'}), required=False)

    class Meta: 
        model = Editorial
        fields = '__all__'

#VALIDACION DE CAMPO 

    def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado is None:  
            raise forms.ValidationError('Este campo es obligatorio.')
        return estado
# LIBROS 
class LibrosForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'ID'}))
    titulo = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'TITULO'}))
    id_autor = forms.ModelChoiceField(queryset=Autor.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))  
    fpublicacion = forms.DateField(widget=forms.SelectDateWidget(years=range(1800, 2034), attrs={'class': 'form-control', 'placeholder': 'FECHA DE PUBLICACIÓN'})
    )
    id_editorial = forms.ModelChoiceField(queryset=Editorial.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}), required=False)
    stock = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'STOCK'}))
    nro_paginas = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'NRO PAGINAS'}))
    
     # ChoiceField para usar el choices definido
    IDIOMA_CHOICES = [
        (0, 'Español'),  # Cambié el orden para que el primer elemento sea el valor y el segundo la etiqueta
        (1, 'Inglés'),
        (2, 'Portugués'),
    ]
    idioma = forms.ChoiceField(choices=IDIOMA_CHOICES, label='Idioma')    

    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'ESTADO'}), required=False)

    class Meta:
        model = Libros
        fields = '__all__'
#Verificacion de campo Estado
def clean_estado(self):
        estado = self.cleaned_data.get('estado')
        if estado is None: 
            raise forms.ValidationError('Este campo es obligatorio y debe ser un número entero.')
        return estado

# AUTOR
class AutorForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'ID'}))
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'NOMBRE'}))
    biografia = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'BIOGRAFIA'}))
    fnacimiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1800, 2034), attrs={'class': 'form-control', 'placeholder':'FECHA NACIMIENTO'}))
    nacionalidad = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'NACIONALIDAD'}))
    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'ESTADO'}))

    class Meta:  
        model = Autor
        fields = '__all__'

# ROL
class RolForm(forms.ModelForm):
    id = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'ID'}))
    estado = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'ESTADO'}), required=False)  
    nombre = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'NACIONALIDAD'}))
    class Meta:  
        model = Rol
        fields = '__all__'