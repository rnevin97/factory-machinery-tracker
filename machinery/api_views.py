
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Machine, RepairRequest, MaintenanceRecord, Warning, UserProfile, Company
from .serializers import (
    MachineSerializer,
    RepairRequestSerializer,
    MaintenanceRecordSerializer,
    WarningSerializer,
    UserSerializer,
    UserProfileSerializer,
)
from .permissions import IsManagerOrTechnician, IsTechnicianOrRepair

# ----------------- ViewSets -----------------

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsManagerOrTechnician]

class RepairRequestViewSet(viewsets.ModelViewSet):
    queryset = RepairRequest.objects.all()
    serializer_class = RepairRequestSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTechnicianOrRepair]

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsManagerOrTechnician]

class WarningViewSet(viewsets.ModelViewSet):
    queryset = Warning.objects.all()
    serializer_class = WarningSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsTechnicianOrRepair]

# ----------------- Auth API -----------------

@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    request.session['id'] = user.id
    if user:
        token, created = Token.objects.get_or_create(user=user)
        try:
            role = UserProfile.objects.get(user=user).role
            request.session['user_role'] = role
        except UserProfile.DoesNotExist:
            role = None
        return Response({'token': token.key, 'role': role, "redirect_url": "/dashboard"})
    
    return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def logout_user(request):
    if request.auth:
        request.auth.delete()
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

# ----------------- Registration API -----------------

class RegistrationAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "Use POST to register a new user."})

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        role = request.data.get('role')
        firstName = request.data.get('firstName')
        lastName = request.data.get('lastName')
        company = request.data.get('companyName')
        
        if User.objects.filter(username=username).exists():
            return Response({'error': 'Username already exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email, first_name=firstName, last_name=lastName)
        UserProfile.objects.create(user=user, role=role)
        Company.objects.create(name=company, email=email, job_title=role, user_id=user.id)
        Token.objects.create(user=user)

        return Response({'message': 'User registered successfully.', "redirect_url": "/login"}, status=status.HTTP_201_CREATED)



@api_view(['GET'])
def getDashboardData(request):

    user_id = request.session.get('id')
    
    # Getting all available machines
    company_name = Company.objects.get(user=user_id).name
    company_ids = Company.objects.filter(name=company_name).values_list('id', flat=True)
    data_available_machines = Machine.objects.filter(company_id__in=company_ids)

    # Getting all available technicians
    users= User.objects.filter(
        id__in=Company.objects.filter(
            name=company_name
        ).values_list('user_id', flat=True),
        userprofile__role='Technician'
    )
    data_available_technicians = [{"id": u.id, "username": u.username, "first_name":u.first_name, "last_name" : u.last_name, "email": u.email, "date_joined": u.date_joined} for u in users]

    # Getting all repair requests
    machine_ids = Machine.objects.filter(company_id__in=company_ids).values_list('id', flat=True)
    data_repair_requests = RepairRequest.objects.filter(machine_id__in=machine_ids)

    machines_serialized = MachineSerializer(data_available_machines, many=True).data
    user_serialized = UserSerializer(data_available_technicians, many=True).data
    requests_serialized = RepairRequestSerializer(data_repair_requests, many=True).data

    data = {
        'machines': machines_serialized,
        'technicians': user_serialized,
        'repairRequests': requests_serialized
    }
    return Response(data)
