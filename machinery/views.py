from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Machine, Company
from .forms import MachineForm
from django.contrib.auth.models import User

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
    company_name = Company.objects.get(user=request.session.get('id')).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    data = Machine.objects.filter(company_id__in=company_ids)
    return render(request, "machinery/machines.html", {'data': data})

def technicians(request):
    
    company_name = Company.objects.get(user=request.session.get('id')).name
    users= User.objects.filter(
        id__in=Company.objects.filter(
            name=company_name
        ).values_list('user_id', flat=True),
        userprofile__role='Technician'
    )
    user_data = [{"id": u.id, "userName": u.username, "firstName":u.first_name, "lastName" : u.last_name, "email": u.email, "dateJoined": u.date_joined} for u in users]
    return render(request, "machinery/technicians.html" , {'data':user_data})


def addMachine(request):
    form = MachineForm
    if request.method == 'POST':
        saveForm = MachineForm(request.POST)
        if saveForm.is_valid():
            machine = saveForm.save(commit=False)
            company = Company.objects.get(user=request.session.get('id')).id
            machine.company_id = company
            machine.save()
            return HttpResponseRedirect("/machines")
    return render(request, "machinery/addMachine.html", {'form': form})


def modifyMachine(request, id):
    machine = Machine.objects.get(id=id)
    form = MachineForm(instance=machine)

    if request.method == 'POST':
        saveForm = MachineForm(request.POST, instance=machine)
        if saveForm.is_valid():
            machine = saveForm.save(commit=False)
            company = Company.objects.get(user=request.session.get('id')).id
            machine.company_id = company
            machine.save()
            return HttpResponseRedirect("/machines")

    return render(request, "machinery/modifyMachine.html", {
        'form': form,
        'machine': machine
    })


def deleteMachine(request, id):
    Machine.objects.filter(id=id).delete()
    return HttpResponseRedirect("/machines")
