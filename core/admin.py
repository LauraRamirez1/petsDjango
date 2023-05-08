from django.contrib import admin
from .models import Cliente, Producto, Servicio, Mascota

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Producto)
admin.site.register(Servicio)
admin.site.register(Mascota)