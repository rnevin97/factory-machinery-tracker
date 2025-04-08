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
    path("dashboard", views.dashboard, name="dashboard"),
    path("machines", views.machines, name="machines"),
    path("technicians", views.technicians, name="technicians"),
    path("addMachine", views.addMachine, name="addMachine"),
    path("deleteMachine/<int:id>", views.deleteMachine, name="deleteMachine"),
]