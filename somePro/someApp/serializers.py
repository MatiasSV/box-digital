from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import RedHospitalaria, Establecimiento, Estamento, Profesional, Box, Registro, FuncionarioSome, Reserva
from .permissions import is_funcionario, is_profesional

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar roles personalizados al token para que el frontend los lea
        token['is_funcionario_some'] = is_funcionario(user)
        token['is_profesional'] = is_profesional(user)
        token['email'] = user.email

        return token

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
