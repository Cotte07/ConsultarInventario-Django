from django.shortcuts import render

# Create your views here.

def agregarProductoNuevo(request):       #vista para mostrar la pagina de agregar producto nuevo
    return render(request, 'agregarproductonuevo.html')