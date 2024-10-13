from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import Producto
from django.http.response import JsonResponse


# Create your views here.

def paginaPrincipal(request):
    return render(request, 'PaginaPrincipal.html')

def lista_producto(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'PaginaPrincipal.html', context)

def exit(request):
    logout(request)
    return redirect('paginaPrincipal')