from django.urls import URLPattern, path
from .views import home
from .views import form
from .views import create
from .views import realizarregistro

urlpatterns = [
    path('', home, name="home"),
    path('home', home, name="home"),
    path('form', form, name="form"),
    path('create', create, name="create"),
    path('realizarregistro',realizarregistro, name="realizarregistro" )

]
