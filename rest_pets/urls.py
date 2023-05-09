from django.urls import path
from .views import lista_mascotas
from .views import lista_productos




urlpatterns = [
    path('lista', lista_mascotas, name="lista"),
    path('lista', lista_productos, name="lista"),
]
