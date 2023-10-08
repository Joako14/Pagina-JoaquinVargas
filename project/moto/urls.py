from django.urls import path
from . import views

app_name = "moto"

urlpatterns = [
    path("", views.index, name="index"),
    path("ingresar_motocicleta", views.ingresar_motocicleta, name="ingresar_motocicleta"),
    path("ingresar_bateria", views.ingresar_bateria, name="ingresar_bateria"),
]