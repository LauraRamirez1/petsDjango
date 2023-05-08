from django.db.models.base import Model
from rest_framework import serializers
from core.models import Mascota

class MascotaSerializer(serializers.MascotaSerializer):
    class Meta:
        model = Mascota
        fields = ['nombreMascota', 'razaMascota']