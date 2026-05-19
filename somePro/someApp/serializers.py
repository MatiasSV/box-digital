from rest_framework import serializers
from .models import RedHospitalaria, Establecimiento, Estamento, Profesional, Box, Registro, FuncionarioSome, Reserva

class RedHospitalariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RedHospitalaria
        fields = '__all__'

class EstablecimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Establecimiento
        fields = '__all__'

class EstamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estamento
        fields = '__all__'

class ProfesionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profesional
        fields = '__all__'

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = '__all__'

class RegistroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registro
        fields = '__all__'

class FuncionarioSomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuncionarioSome
        fields = '__all__'

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = '__all__'
