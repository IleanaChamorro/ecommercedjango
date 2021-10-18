from django.shortcuts import render
from blog.models import Noticias,Categoria
# Create your views here.
def blog(request):
    noticias=Noticias.objects.all()
    return render(request, 'blog/blog.html', {"noticias":noticias})

def categoria(request, categoria_id):
    #Listar post correspondientes a categoria
    categoria=Categoria.objects.get(id=categoria_id)
    #Mostrar los post 
    noticias=Noticias.objects.filter(categorias=categoria)
    return render(request, "blog/categorias.html", {'categoria': categoria, "noticias": noticias})