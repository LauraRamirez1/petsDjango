from django.db import models

# Create your models here.
class Cliente(models.Model):
        codigoCliente = models.AutoField(primary_key=True)
        nombre = models.CharField(max_length=30)
        telefono = models.CharField(max_length=50)
        correo = models.CharField(max_length=50)
        password = models.CharField(max_length=30)


        def __str__(self):
                return self.nombre


class Producto(models.Model):
        nombreProducto = models.CharField(max_length=50)
        precioProducto = models.IntegerField()
        descripcionProducto = models.TextField()
        
        def __str__(self):
                return self.nombreProducto
                
class Servicio(models.Model):
        nombreServicio = models.CharField(max_length=50)
        precioServicio = models.IntegerField()
        descripcionServicio = models.TextField()
        
        def __str__(self):
                return self.nombreServicio
                
class Mascota(models.Model):
        nombreMascota = models.CharField(max_length=50)
        edadMascota = models.IntegerField()
        razaMascota = models.CharField(max_length=50)
        nombre = models.ForeignKey(Cliente, on_delete=models.CASCADE)
        
        def __str__(self):
                return self.nombreMascota
                
