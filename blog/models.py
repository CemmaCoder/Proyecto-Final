from django.db import models
from ckeditor.fields import RichTextField

# ---------------------------------

# Clase padre 
class Base(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField('Estado', default=True)
    fecha_creacion = models.DateTimeField('Fecha de Creacion', null=True, blank=True)

# Para que no se guarde en nuestra base de datos
    class Meta:
        abstract = True

# ---------------------------------

class Autor(Base):
    nombre = models.CharField('Nombre de Autor', max_length=100, null=False, blank=False)
    apellido = models.CharField('Apellido de Autor', max_length=100, null=False, blank=False)
    correo = models.EmailField('Correo de Autor', max_length=100, null=False, blank=False)

# Define un nombre singular/plural del modelo (Usado para el panel de admin django)
    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

# Metodo legible para nuestro modelo
    def __str__(self):
        return f' {self.apellido}, {self.nombre}'

# ---------------------------------

class Categoria(Base):
    nombre = models.CharField('Nombre de la Categoria', max_length=255, unique=True)

# Define un nombre singular/plural del modelo (Usado para el panel de admin django)
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

# Metodo legible para nuestro modelo
    def __str__(self):
        return self.nombre

# ---------------------------------

class Post(Base):
    titulo = models.CharField('Nombre del Post', max_length=100, unique=True, null = False, blank = False)
    descripcion = models.CharField('Descripcion', max_length= 100, null = False, blank = False)
    contenido = RichTextField(null = True)
    imagen = models.URLField('Imagen', max_length=100, null = True, blank = True)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE)

# Define un nombre singular/plural del modelo (Usado para el panel de admin django)
# Ordenar post
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-fecha_creacion']

# Metodo legible para nuestro modelo
    def __str__(self):
        return self.titulo

# ---------------------------------

opciones_contacto = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Segurencia"],
    [3, "Feliciaciones"]
    ]

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    tipo_contacto = models.IntegerField(choices= opciones_contacto)
    mensaje = models.TextField()
    avisos = models.BooleanField()

# Metodo legible para nuestro modelo
    def __str__(self):
        return self.nombre

# ---------------------------------

class SobreMi(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = RichTextField(null = True)

# Metodo legible para nuestro modelo
    def __str__(self):
        return self.titulo

# ---------------------------------
