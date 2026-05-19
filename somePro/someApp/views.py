from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import RedHospitalaria, Establecimiento, Estamento, Profesional, Box, Registro
from .serializers import (
    RedHospitalariaSerializer,
    EstablecimientoSerializer,
    EstamentoSerializer,
    ProfesionalSerializer,
    BoxSerializer,
    RegistroSerializer
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

# Create your views here.
