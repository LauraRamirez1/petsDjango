from django.db.models.base import Model
from rest_framework import serializers
from core.models import Mascota
from core.models import Producto

class MascotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mascota
        fields = ['nombreMascota', 'razaMascota']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombreProducto', 'precioProducto']