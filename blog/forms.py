from dataclasses import field
from django import forms
from .models import *
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# ---------------------------------
class AutorForm(forms.Form):

    class Meta:
        model = Autor
        fields = '__all__'     # IMPORTA TODOS LOS CAMPOS MENCIONADOS EN EL MODELO

# ---------------------------------
class PostForm(forms.Form):

    class Meta:
        model = Post
        fields = '__all__'     # IMPORTA TODOS LOS CAMPOS MENCIONADOS EN EL MODELO

# ---------------------------------

class ContactoForm(forms.ModelForm):

    class Meta:
        model = Contacto
        fields = '__all__'     # IMPORTA TODOS LOS CAMPOS MENCIONADOS EN EL MODELO

# ---------------------------------

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        help_texts = {k: "" for k in fields}

# ---------------------------------

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Modificar contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar contraseña', widget= forms.PasswordInput)
    first_name = forms.CharField(label='Modificar Nombre')
    last_name = forms.CharField(label='Modificar Apellido')

    class Meta:
        model = User
        fields = [ 'username', 'email', 'password1', 'password2', 'first_name', 'last_name',]
        help_texts = {k: "" for k in fields}

# ---------------------------------