from django.shortcuts import render, redirect
from .carrito import Carro
from tienda.models import Producto

# Create your views here.
def agregar_producto(request, productos_id):
    carrito=Carro(request)
    producto=Producto.objects.get(id=productos_id)
    carrito.agregar(producto=producto)
    return redirect("tienda")

def eliminar_producto(request, productos_id):
    carrito=Carro(request)
    producto=Producto.objects.get(id=productos_id)
    carrito.eliminar_items(producto=producto)
    return redirect("tienda")

def quitar_producto(request, productos_id):
    carrito=Carro(request)
    producto=Producto.objects.get(id=productos_id)
    carrito.quitar_producto(producto=producto)
    return redirect("tienda")

def limpiar_carro(request, productos_id):
    carrito=Carro(request)
    carrito.limpiar_carro()
    return redirect("tienda")