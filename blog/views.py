from django.shortcuts import render
from blog.models import Noticias

# Create your views here.
def blog(request):
    noticias=Noticias.objects.all()
    return render(request, 'blog/blog.html', {"noticias":noticias})