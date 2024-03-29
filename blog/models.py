from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre=models.CharField(max_length=60)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="categoria"
        verbose_name="categorias"

    def __str__(self):
        return self.nombre

    
class Noticias(models.Model):
    titulo=models.CharField(max_length=200)
    contenido=models.CharField(max_length=400)
    imagen=models.ImageField(upload_to="blog", null=True, blank=True)
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    categorias=models.ManyToManyField(Categoria)
    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name="noticia"
        verbose_name="noticias"

    def __str__(self):
       return self.titulo