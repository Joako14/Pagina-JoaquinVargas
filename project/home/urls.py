from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", LoginView.as_view(template_name="home/login.html", next_page="home:index"), name="login"),
    path("logout/", LogoutView.as_view(template_name="home/logout.html"), name="logout"),
]