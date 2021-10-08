from django.shortcuts import render, HttpResponse
from servicios.models import Servicio

# Create your views here.
def inicio(request):

    return render(request, 'ProjectEcomApp/inicio.html')
def servicios(request):
    servicios=Servicio.objects.all()
    return render(request, 'ProjectEcomApp/servicios.html', {"servicios": servicios})
def tienda(request):

    return render(request, 'ProjectEcomApp/tienda.html')
def contacto(request):

    return render(request, 'ProjectEcomApp/contacto.html')
def info(request):

    return render(request, 'ProjectEcomApp/info.html')