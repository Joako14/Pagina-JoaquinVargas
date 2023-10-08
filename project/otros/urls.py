from django.urls import path
from . import views

app_name = "otros"

urlpatterns = [
    path("", views.index, name="index"),
    path("ingresar_equipo", views.ingresar_equipo, name="ingresar_equipo"),
    path("ingresar_bateria", views.ingresar_bateria, name="ingresar_bateria"),
]