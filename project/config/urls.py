from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("", include("home.urls")),
    path("catalogo/", include("catalogo.urls")),
]