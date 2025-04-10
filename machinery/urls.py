from django.urls import path
from . import views
from . import api_views  # 👈 new import for your API views
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
    path("technicians", views.technicians, name="technicians"),
    path("machines", views.machines, name="machines"),
    path("addMachine", views.addMachine, name="addMachine"),
    path("deleteMachine/<int:id>", views.deleteMachine, name="deleteMachine"),
    path("modifyMachine/<int:id>/", views.modifyMachine, name="modifyMachine"),
    path("repairRequests", views.repairRequests, name="repairRequests"),
    path("addRepairRequest", views.addRepairRequest, name="addRepairRequest"),
    path("deleteRepairRequest/<int:id>", views.deleteRepairRequest, name="deleteRepairRequest"),
    path("modifyRepairRequest/<int:id>/", views.modifyRepairRequest, name="modifyRepairRequest"),


    # API Routes (from api_views)
    path("api/login/", api_views.login_user, name="api_login"),
    path("api/logout/", api_views.logout_user, name="api_logout"),
    path("api/register/", api_views.RegistrationAPIView.as_view(), name="api_register"),
    path("api/token-auth/", obtain_auth_token),
]
