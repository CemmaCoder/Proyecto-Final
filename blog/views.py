from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.core.paginator import Paginator


# ListView
class Inicio(ListView):

    def get(self,request):
        post_parches = Post.objects.filter( categoria = Categoria.objects.get(nombre= 'Parches')).latest('fecha_creacion')
        post_noticias = Post.objects.filter( categoria = Categoria.objects.get(nombre= 'Noticias')).latest('fecha_creacion')
        post_sports = Post.objects.filter( categoria = Categoria.objects.get(nombre= 'eSPORTS')).latest('fecha_creacion')
        post_comunidad = Post.objects.filter( categoria = Categoria.objects.get(nombre= 'Comunidad')).latest('fecha_creacion')
        
        contexto = {
            'post_parches': post_parches,
            'post_noticias': post_noticias,
            'post_sports': post_sports,
            'post_comunidad': post_comunidad,
        }

        return render(request, 'index.html', contexto)

class AboutMe(ListView):
    model = SobreMi
    template_name = 'about.html'

# ---------------------------------

# ListView
class ListaPost(ListView):
    model = Post
    template_name = 'post_lista.html'
    queryset = Post.objects.order_by('-fecha_creacion')

# ---------------------------------
class PostParches(ListView):
    model = Post
    template_name = 'parches.html'

    def get_queryset(self):
        return Post.objects.filter(categoria = Categoria.objects.get(nombre= 'Parches')) 

# ---------------------------------
class PostNoticias(ListView):
    model = Post
    template_name = 'noticias.html'

    def get_queryset(self):
        return Post.objects.filter(categoria = Categoria.objects.get(nombre= 'Noticias'))

# ---------------------------------
class PostSports(ListView):
    model = Post
    template_name = 'sports.html'

    def get_queryset(self):
        return Post.objects.filter(categoria = Categoria.objects.get(nombre= 'eSPORTS'))

# ---------------------------------
class PostComunidad(ListView):
    model = Post
    template_name = 'comunidad.html'

    def get_queryset(self):
        return Post.objects.filter(categoria = Categoria.objects.get(nombre= 'Comunidad'))

# ------------------------------------------------------------------------------------------------------------------------

# DetailView
class DetallePost(DetailView):
    model = Post
    template_name = 'post.html'
    

# ---------------------------------

class DetalleAutor(DetailView):
    pass

# ------------------------------------------------------------------------------------------------------------------------

# UpdateView
class EditarPost(UpdateView):
    model = Post
    fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria']
    success_url = reverse_lazy('listar_post')

# ---------------------------------

class EditarAutor(UpdateView):
    pass

# ------------------------------------------------------------------------------------------------------------------------

# DeleteView
class BorrarPost(DeleteView):
    model = Post
    success_url = reverse_lazy('listar_post')

# ---------------------------------
class BorrarAutor(DeleteView):
    pass

# ------------------------------------------------------------------------------------------------------------------------


# CreateView
class CrearPost(CreateView):
    model = Post
    fields = ['titulo', 'descripcion', 'contenido', 'imagen', 'autor', 'categoria', 'fecha_creacion']
    success_url = reverse_lazy('listar_post')

# ---------------------------------
class CrearAutor(CreateView):
    pass

# ------------------------------------------------------------------------------------------------------------------------

# Contacto

data = { 'form' : ContactoForm() }

@login_required
def contacto(request):
    if request.method == 'POST':
        MiFormulario = ContactoForm(data=request.POST)
        if MiFormulario.is_valid():
            MiFormulario.save()
            messages.success(request, "Su mensaje se ha enviado satisfactoriamente")
            return redirect(to='index')
        else:
            data['form'] = MiFormulario
    return render(request, 'contacto.html', data)

# ------------------------------------------------------------------------------------------------------------------------

# LOGEAR

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contraseña = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user is not None:
                login(request, user)
                messages.success(request, "¡ Bienvenido ! ")
                return redirect(to='index')
        else:
            return render(request, 'login.html', {'form':form})
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

# ---------------------------------

# REGISTRAR

def register_request(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            # login(request, username)
            messages.success(request, "Usuario Creado")
            return redirect(to='index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form':form})

# ---------------------------------

# LOGOUT

def logout_request(request):
    logout(request)
    messages.success(request, "Te has deslogeado safisfactoriamente")
    return redirect(to='index')

# ---------------------------------

# EDITAR PERFIL USUARIO

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == 'POST':
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            info = form.cleaned_data
            usuario.email = info['email']
            usuario.password1 = info['password1']
            usuario.password2 = info['password2']
            # usuario.first_name = info['first_name']
            # usuario.last_name = info['last_name']
            usuario.save()
            messages.success(request, 'Datos actualizados con exito')
            return redirect(to='index')
    else:
        form = UserEditForm(instance=usuario)
    return render(request, 'editar_perfil.html', {'form': form, 'usuario': usuario.username})

# ---------------------------------
