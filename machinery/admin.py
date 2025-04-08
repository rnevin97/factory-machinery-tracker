from django.contrib import admin
from .models import (
    Company,
    Machine,
    RepairRequest,
    MaintenanceRecord,
    Warning,
    UserProfile,
    MachineCollection
)

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'job_title')
    search_fields = ('name', 'email')

@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    list_display = ('name', 'serial_number', 'company', 'importance', 'status')
    search_fields = ('name', 'serial_number')
    list_filter = ('status', 'importance')

@admin.register(RepairRequest)
class RepairRequestAdmin(admin.ModelAdmin):
    list_display = ('machine', 'status', 'assigned_to', 'created_at', 'resolved')
    search_fields = ('machine__name', 'assigned_to')
    list_filter = ('status', 'resolved')

@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('machine', 'performed_at')
    search_fields = ('machine__name',)
    list_filter = ('performed_at',)

@admin.register(Warning)
class WarningAdmin(admin.ModelAdmin):
    list_display = ('machine', 'message', 'created_at', 'added_by')
    search_fields = ('machine__name', 'message')
    list_filter = ('created_at',)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)

@admin.register(MachineCollection)
class MachineCollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    filter_horizontal = ('machines',)
