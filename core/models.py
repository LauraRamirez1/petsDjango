from django.db import models

# Create your models here.
class Cliente(models.Model):
        codigoCliente = models.AutoField(primary_key=True)
        nombreCliente = models.CharField(max_length=30)
        telefonoCliente = models.IntegerField()
        correoCliente = models.CharField(max_length=50)
        passCliente = models.CharField(max_length=30)


        def __str__(self):
                return self.nombreCliente


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
                
