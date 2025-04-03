from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone


def index(request):
    context = {}
    return render(request, "machinery/index.html",context)

def aboutUs(request):
    context = {}
    return render(request, "machinery/about-us.html",context)

def faqs(request):
    context = {}
    return render(request, "machinery/faqs.html",context)

def login(request):
    context = {}
    return render(request, "machinery/login.html",context)

def register(request):
    context = {}
    return render(request, "machinery/register.html",context)

def services(request):
    context = {}
    return render(request, "machinery/services.html",context)    