from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home", views.index, name="index"),
    path("about-us", views.aboutUs, name="aboutUs"),
    path("faqs", views.faqs, name="faqs"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("services", views.services, name="services"),
]