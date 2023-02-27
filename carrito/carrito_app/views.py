from django.shortcuts import redirect, render, HttpResponse
from carrito_app.Carrito import Carrito
from carrito_app.models import Producto

# Create your views here.

def inicio(request):
    productos = Producto.objects.all()
    return render(request, 'inicio.html', {'productos': productos})
    #return HttpResponse('HOLA')

def agregar_al_carrito(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.agregar_producto(producto)
    return redirect('inicio')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.eliminar_producto(producto)
    return redirect('iniciol')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id = producto_id)
    carrito.quitar_producto(producto)
    return redirect('inicio')

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar_carrito()
    return redirect('inicio')





