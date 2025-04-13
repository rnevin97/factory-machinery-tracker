from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Machine, Company, RepairRequest
from .forms import MachineForm, RepairRequestForm
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

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
    total_machines = Machine.objects.count()
    total_repairs = RepairRequest.objects.count()

    return render(request, "machinery/dashboard.html", {
        'total_machines': total_machines,
        'repair_requests': total_repairs
    })

def logoutUser(request):
    logout(request)
    return redirect('/login')

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

def machines(request):
    company_name = Company.objects.get(user=request.session.get('id')).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    data = Machine.objects.filter(company_id__in=company_ids)
    return render(request, "machinery/machines.html", {'data': data})

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


def repairRequests(request):
    # only getting repairRequests which are raised against machines which are part of user company
    company_name = Company.objects.get(user=request.session.get('id')).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    machine_ids = Machine.objects.filter(company_id__in=company_ids).values_list('id', flat=True)
    data = RepairRequest.objects.filter(machine_id__in=machine_ids)

    return render(request, "machinery/repairRequests.html", {'data': data})


def addRepairRequest(request):
    # Getting machines which are part of the user company
    company_name = Company.objects.get(user=request.session.get('id')).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    machines = Machine.objects.filter(company_id__in=company_ids)

    if request.method == 'POST':
        user_id = request.session.get('id')
        user = User.objects.get(id=user_id)
        form = RepairRequestForm(request.POST)
        if form.is_valid():
            repair_request = form.save(commit=False)
            repair_request.raised_by = user
            repair_request.assigned_to = 'Unassigned'
            repair_request.save()
            return HttpResponseRedirect("/repairRequests")
    else:
        form = RepairRequestForm()
        form.fields['machine'].queryset = machines

    return render(request, 'machinery/addRepairRequest.html', {'form': form})


def modifyRepairRequest(request, id):
    # Getting machines which are part of the user company
    company_name = Company.objects.get(user=request.session.get('id')).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    machines = Machine.objects.filter(company_id__in=company_ids)

    repairRequest = RepairRequest.objects.get(id=id)
    form = RepairRequestForm(instance=repairRequest)
    user_id = request.session.get('id')
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        saveForm = RepairRequestForm(request.POST, instance=repairRequest)
        if saveForm.is_valid():
            repairRequest = saveForm.save(commit=False)
            repairRequest.raised_by = user
            repairRequest.assigned_to = 'Unassigned'
            repairRequest.save()
            return HttpResponseRedirect("/repairRequests")
    else:
        form.fields['machine'].queryset = machines 
    
    return render(request, "machinery/modifyRepairRequest.html", {
        'form': form,
        'request': repairRequest
    })


def deleteRepairRequest(request, id):
    RepairRequest.objects.filter(id=id).delete()
    return HttpResponseRedirect("/repairRequests")