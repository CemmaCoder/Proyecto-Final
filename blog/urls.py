from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import  Inicio, PostParches, PostNoticias, PostSports, PostComunidad, \
                    CrearPost, DetallePost, EditarPost, BorrarPost, ListaPost, AboutMe, \
                    login_request, register_request, logout_request, editarPerfil, contacto


urlpatterns = [
    path('', Inicio.as_view(), name = 'index'),
    path('parches/', PostParches.as_view(), name = 'parches'),
    path('noticias/', PostNoticias.as_view(), name = 'noticias'),
    path('sports/', PostSports.as_view(), name = 'sports'),
    path('comunidad/', PostComunidad.as_view(), name = 'comunidad'),
    path('post/<int:pk>/', DetallePost.as_view(), name = 'detalle_post'),
    path('about/', AboutMe.as_view(), name = 'sobre_mi'),

    path('post/list/', ListaPost.as_view(), name = 'listar_post'),
    path('post/new/', CrearPost.as_view(), name = 'crear_post'),
    path('post/update/<int:pk>/', EditarPost.as_view(), name = 'editar_post'),
    path('post/delete/<int:pk>/', BorrarPost.as_view(), name = 'borrar_post'),

    path('contacto/', contacto, name = 'contacto'),
    path('accounts/registro/', register_request, name='registro'),
    path('accounts/login', login_request, name='login'),
    path('accounts/logout', logout_request, name='logout'),
    # path('accounts/profile/', profile_request, name='profile'),
    path('accounts/editar', editarPerfil, name='editar_perfil'),
    ]
