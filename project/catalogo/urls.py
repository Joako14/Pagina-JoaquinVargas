from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", TemplateView.as_view(template_name = "catalogo/index.html"), name = "index"),
    path("catalogo/list/", views.CatalogoList.as_view(), name = "catalogo_list"),
    path("catalogo/create/", views.CatalogoCreate.as_view(), name = "catalogo_form"),
    path("catalogo/createmarca/", views.MarcaCategoriaCreate.as_view(), name = "marcacategoria_form"),
    path("catalogo/createmodelo/", views.ModeloCategoriaCreate.as_view(), name = "modelocategoria_form"),
    path("catalogo/createaño/", views.AñoCategoriaCreate.as_view(), name = "añocategoria_form"),
    path("catalogo/createbateria/", views.BateriaCategoriaCreate.as_view(), name = "bateriacategoria_form"),
    path("catalogo/catalogoupdate/<int:pk>", views.CatalogoUpdate.as_view(), name = "catalogo_update"),
    path("catalogo/catalogodelete/<int:pk>", views.CatalogoDelete.as_view(), name = "catalogo_delete"),
    path("catalogo/detail/<int:pk>", views.CatalogoDetail.as_view(), name = "catalogo_detail"),
    path('consulta/', views.consulta_catalogo, name='consulta_catalogo'),
]