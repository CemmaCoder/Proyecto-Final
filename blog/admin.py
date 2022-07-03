from re import search
from django.contrib import admin
from .models import Autor, Categoria, Post, Contacto, SobreMi

# -----------------------

# Actulizacion en el panel admin django (Visualizar atributos y Barra de busqueda)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion')

class AutorAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'apellido', 'correo']
    list_display= ('nombre','apellido', 'correo', 'estado','fecha_creacion')

class PostAdmin(admin.ModelAdmin):
    search_fields = ['titulo', 'autor', 'categoria', 'fecha_creacion']
    list_display = ('titulo', 'autor', 'categoria', 'fecha_creacion')

class ContactoAdmin(admin.ModelAdmin):
    search_fields = ['nombre', 'correo', 'tipo_contacto']
    list_display = ('nombre', 'correo', 'tipo_contacto')

# -----------------------

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(SobreMi)