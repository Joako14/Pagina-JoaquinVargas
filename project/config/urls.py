from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path("", include("home.urls")),
    path("moto/", include("moto.urls")),
    path("auto/", include("auto.urls")),
    path("otros/", include("otros.urls")),
    path("catalogo/", include("catalogo.urls")),
]