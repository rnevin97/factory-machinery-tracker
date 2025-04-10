from django.db import models
from django.contrib.auth.models import User

class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    job_title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Machine(models.Model):
    name = models.CharField(max_length=100)
    serial_number = models.CharField(max_length=100, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    importance = models.IntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"

class RepairRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]
    issue_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    assigned_to = models.CharField(max_length=100)  # You can also use FK to User
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    raised_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='repair_requests')
    resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"Repair #{self.id} for {self.machine.name}"

class MaintenanceRecord(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    description = models.TextField()
    performed_at = models.DateTimeField()

    def __str__(self):
        return f"Maintenance for {self.machine.name} on {self.performed_at.date()}"

class Warning(models.Model):
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    added_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Warning on {self.machine.name}: {self.message}"

class UserProfile(models.Model):
    ROLE_CHOICES = [
        ('manager', 'Manager'),
        ('technician', 'Technician'),
        ('repair_person', 'Repair Person'),
        ('admin', 'Admin'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} - {self.role}"

class MachineCollection(models.Model):
    name = models.CharField(max_length=100, unique=True)
    machines = models.ManyToManyField(Machine)

    def __str__(self):
        return self.name
