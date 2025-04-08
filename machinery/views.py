from django.http import HttpResponse , HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from .models import Machine
from .forms import MachineForm


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

def dashboard(request):
    context = {}
    return render(request, "machinery/dashboard.html",context)  


def machines(request):
    data = Machine.objects.all();
    context = {
        'data' : data
    }
    return render(request, "machinery/machines.html",context)



def technicians(request):
    context = {
    }
    return render(request, "machinery/technicians.html",context)

    

def addMachine(request):
    form =  MachineForm
    if request.method == 'POST':
        saveForm = MachineForm(request.POST)
        if saveForm.is_valid():
            saveForm.save();
            return HttpResponseRedirect("/machines")

    return render(request, "machinery/addMachine.html",{'form' : form})

def deleteMachine(request , id) :
    Machine.objects.filter(id=id).delete()
    return HttpResponseRedirect("/machines")