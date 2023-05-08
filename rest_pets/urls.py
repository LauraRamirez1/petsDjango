from django.urls import path
from .views import listaMascotas




urlpatterns = [
    path('lista', listaMascotas, name="lista"),


]
