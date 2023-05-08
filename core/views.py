from django.shortcuts import render,redirect
from .models import Cliente
from .models import Producto
from .models import Servicio
from .models import Mascota

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
    nombre_c = request.POST['nombre']
    telefono_c = request.POST['telefono']
    correo_c = request.POST['correo']
    password_c = request.POST['password']

    #insert en tabla
    Cliente.objects.create(nombre = nombre_c, telefono = telefono_c, correo = correo_c, password = password_c)
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

def listaMascotas(request):
    mascotas = Mascota.objects.all() #select * from Mascota;
    contexto = {"mascotas": mascotas}
    return render(request,'core/listaMascotas.html', contexto)

def agregarMascota(request):
    clientes = Cliente.objects.all()
    contexto = {"cliente": clientes}
    return render(request,'core/agregarMascota.html', contexto)

def agregarRegistroMascota(request):
    nombreMascota_c = request.POST['nombreMascota']
    edadMascota_c = request.POST['edadMascota']
    razaMascota_c = request.POST['razaMascota']
    nombre_c = request.POST['nombre']


    #traer registro completo de clientes
    nombre_c = Cliente.objects.get(codigoCliente = nombre_c)

    #insert
    Mascota.objects.create(
        nombreMascota = nombreMascota_c,
        edadMascota = edadMascota_c,
        razaMascota = razaMascota_c,
        nombre = nombre_c

    )
    return redirect('agregarMascota')


def eliminarMascota(request, nombreMascota):
    mascota1 = Mascota.objects.get(nombreMascota = nombreMascota) #producto a eliminar
    mascota1.delete() #elimina el registro obtenido de la BD
    messages.success(request, 'Mascota eliminada')
    return redirect('listaMascotas')




