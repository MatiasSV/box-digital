from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RedHospitalaria, Establecimiento, Estamento, Profesional, Box, Registro, FuncionarioSome, Reserva
from .serializers import (
    RedHospitalariaSerializer,
    EstablecimientoSerializer,
    EstamentoSerializer,
    ProfesionalSerializer,
    BoxSerializer,
    RegistroSerializer,
    FuncionarioSomeSerializer,
    ReservaSerializer
)

class RedHospitalariaViewSet(viewsets.ModelViewSet):
    queryset = RedHospitalaria.objects.all()
    serializer_class = RedHospitalariaSerializer
    permission_classes = [IsAuthenticated]

class EstablecimientoViewSet(viewsets.ModelViewSet):
    queryset = Establecimiento.objects.all()
    serializer_class = EstablecimientoSerializer
    permission_classes = [IsAuthenticated]

class EstamentoViewSet(viewsets.ModelViewSet):
    queryset = Estamento.objects.all()
    serializer_class = EstamentoSerializer
    permission_classes = [IsAuthenticated]

class ProfesionalViewSet(viewsets.ModelViewSet):
    queryset = Profesional.objects.all()
    serializer_class = ProfesionalSerializer
    permission_classes = [IsAuthenticated]

class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer
    permission_classes = [IsAuthenticated]

class RegistroViewSet(viewsets.ModelViewSet):
    queryset = Registro.objects.all()
    serializer_class = RegistroSerializer
    permission_classes = [IsAuthenticated]

class FuncionarioSomeViewSet(viewsets.ModelViewSet):
    queryset = FuncionarioSome.objects.all()
    serializer_class = FuncionarioSomeSerializer
    permission_classes = [IsAuthenticated]

class ReservaViewSet(viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer
    permission_classes = [IsAuthenticated]

def get_establecimientos(request):
    red_id = request.GET.get('red_id')
    establecimientos = Establecimiento.objects.filter(red_id=red_id).values('id', 'nombre_establecimiento') if red_id else []
    return JsonResponse(list(establecimientos), safe=False)

def get_estamentos(request):
    establecimiento_id = request.GET.get('establecimiento_id')
    estamentos = Estamento.objects.filter(establecimiento_id=establecimiento_id).values('id', 'nombre_estamento') if establecimiento_id else []
    return JsonResponse(list(estamentos), safe=False)
