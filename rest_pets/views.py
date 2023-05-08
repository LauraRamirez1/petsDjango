from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from core.models import Mascota
from .serializers import MascotaSerializer

# Create your views here.
@csrf_exempt
@api_view(['GET', 'POST'])

def lista_mascotas(request):
    if request.method == 'GET':
        mascotas = Mascota.objects.all()
        serializer = MascotaSerializer(mascotas, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MascotaSerializer(data = data)
        