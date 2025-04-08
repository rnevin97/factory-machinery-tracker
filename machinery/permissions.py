from rest_framework.permissions import BasePermission
from .models import UserProfile

class IsManagerOrTechnician(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                return profile.role in ['manager', 'technician']
            except UserProfile.DoesNotExist:
                return False
        return False

class IsTechnicianOrRepair(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                return profile.role in ['technician', 'repair_person']
            except UserProfile.DoesNotExist:
                return False
        return False
