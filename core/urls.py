from django.urls import URLPattern, path
from .views import home
from .views import form
from .views import create
from .views import realizarregistro
from .views import listaServicios
from .views import listaProductos
from .views import eliminarProducto
from .views import eliminarServicio
from .views import listaMascotas
from .views import agregarMascota
from .views import agregarRegistroMascota
from .views import eliminarMascota




urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('form', form, name="form"),
    path('create', create, name="create"),
    path('realizarregistro',realizarregistro, name="realizarregistro" ),
    path('listaServicios',listaServicios, name="listaServicios" ),
    path('listaProductos',listaProductos, name="listaProductos" ),
    path('eliminarProducto/<nombreProducto>',eliminarProducto, name="eliminarProducto" ),
    path('eliminarServicio/<nombreServicio>',eliminarServicio, name="eliminarServicio" ),
    path('listaMascotas',listaMascotas, name="listaMascotas" ),
    path('agregarMascota',agregarMascota, name="agregarMascota" ),
    path('agregarRegistroMascota',agregarRegistroMascota, name="agregarRegistroMascota" ),
    path('eliminarMascota/<nombreMascota>',eliminarMascota, name="eliminarMascota" ),

]
