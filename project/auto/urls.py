from django.urls import path
from . import views

app_name = "auto"

urlpatterns = [
    path("", views.index, name="index"),
    path("ingresar_vehiculo", views.ingresar_vehiculo, name="ingresar_vehiculo"),
    path("ingresar_bateria", views.ingresar_bateria, name="ingresar_bateria"),
]