from django.urls import path
from . import views
from .views import login_user, logout_user, RegistrationAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Web App Views
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

    # API Routes
    path("api/login/", login_user, name="api_login"),
    path("api/logout/", logout_user, name="api_logout"),
    path("api/register/", RegistrationAPIView.as_view(), name="api_register"),
    path("api/token-auth/", obtain_auth_token),
]
