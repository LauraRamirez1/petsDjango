from django.shortcuts import render,redirect
from .models import Cliente
from .models import Producto
from .models import Servicio

from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def form(request):
    return render(request,'core/form.html')

def listaServicios(request):
    servicios = Servicio.objects.all() #select * from Mascota;
    contexto = {"servicios": servicios}
    return render(request,'core/listaServicios.html', contexto)


def listaProductos(request):
    productos = Producto.objects.all() #select * from Mascota;
    contexto = {"productos": productos}
    return render(request,'core/listaProductos.html', contexto)

def create(request):
    return render(request,'core/create.html')

def realizarregistro(request):
    nombre = request.POST['nombre']
    telefono = request.POST['telefono']
    correo = request.POST['correo']
    password = request.POST['password']

    #insert en tabla
    Cliente.objects.create(nombreCliente = nombre, telefonoCliente = telefono, correoCliente = correo, passCliente = password)
    messages.success(request, 'Cliente registrado')
    return redirect('create')


def eliminarProducto(request, nombreProducto):
    producto1 = Producto.objects.get(nombreProducto = nombreProducto) #producto a eliminar
    producto1.delete() #elimina el registro obtenido de la BD
    messages.success(request, 'Producto eliminado')
    return redirect('listaProductos')

def eliminarServicio(request, nombreServicio):
    servicio1 = Servicio.objects.get(nombreServicio = nombreServicio) #producto a eliminar
    servicio1.delete() #elimina el registro obtenido de la BD
    messages.success(request, 'Servicio eliminado')
    return redirect('listaServicios')





