from django.contrib import admin 
from django.urls import path, include
from .views import vistaPrueba, listaProductos, listaLoteHistorial, inventario_view
from . import views
from rest_framework.routers import DefaultRouter

Vista1 = vistaPrueba.as_view({'get': 'list'})

router = DefaultRouter()
router.register(r'producto',listaProductos)
router.register(r'loteHistorial',listaLoteHistorial)

urlpatterns = [
    path('vista1/', Vista1),
    path('inventario/', inventario_view, name='inventario'),
    path('producto/', include(router.urls))
]