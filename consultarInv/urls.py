from django.contrib import admin 
from django.urls import path, include
from .views import  listaProductos, inventario_view
from rest_framework.routers import DefaultRouter
from .import views


router = DefaultRouter()
router.register(r'producto',listaProductos)

urlpatterns = [
    path('inventario/', inventario_view, name='inventario'),
    path('producto/', include(router.urls)),
    path('guardarDatos/', views.guardar_datos, name='guardar_datos')
]