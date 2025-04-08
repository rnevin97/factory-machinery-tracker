from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Machine
from .forms import MachineForm

def index(request):
    return render(request, "machinery/index.html")

def aboutUs(request):
    return render(request, "machinery/about-us.html")

def faqs(request):
    return render(request, "machinery/faqs.html")

def login(request):
    return render(request, "machinery/login.html")

def register(request):
    return render(request, "machinery/register.html")

def services(request):
    return render(request, "machinery/services.html")

def dashboard(request):
    return render(request, "machinery/dashboard.html")

def machines(request):
    data = Machine.objects.all()
    return render(request, "machinery/machines.html", {'data': data})

def technicians(request):
    return render(request, "machinery/technicians.html")

def addMachine(request):
    form = MachineForm
    if request.method == 'POST':
        saveForm = MachineForm(request.POST)
        if saveForm.is_valid():
            saveForm.save()
            return HttpResponseRedirect("/machines")
    return render(request, "machinery/addMachine.html", {'form': form})

def deleteMachine(request, id):
    Machine.objects.filter(id=id).delete()
    return HttpResponseRedirect("/machines")
