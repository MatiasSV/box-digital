from datetime import date

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models

class RedHospitalaria(models.Model):
    nombre_red = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_red

class Establecimiento(models.Model):
    nombre_establecimiento = models.CharField(max_length=100)
    tipo_establecimiento = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    ciudad_pueblo_localidad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    fecha_creacion = models.DateField(auto_now_add=True)
    red = models.ForeignKey(RedHospitalaria, on_delete=models.CASCADE, related_name='establecimientos')

    def __str__(self):
        return self.nombre_establecimiento

class Estamento(models.Model):
    nombre_estamento = models.CharField(max_length=100)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='estamentos')

    def __str__(self):
        return self.nombre_estamento

class Profesional(models.Model):
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100 , null=True, blank=True)
    # Creamos la regla: 7 a 8 números, un guion, y un número o la letra 'K' al final
    validador_rut = RegexValidator(
        regex=r'^\d{7,8}-[\dkK]$', 
        message='El RUT debe tener el formato 12345678-9 (sin puntos y con guion).'
    )
    rut = models.CharField(
        max_length=20, 
        unique=True, 
        validators=[validador_rut],
        null=True, # Déjalo si elegiste la opción 2 del paso anterior
        blank=True
    )
    genero = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    ciudad_pueblo_localidad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    universidad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_conexion = models.DateTimeField(auto_now=True)
    red = models.ForeignKey(RedHospitalaria, on_delete=models.CASCADE, null=True, blank=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='funcionarios', null=True, blank=True)
    estamento = models.ForeignKey(Estamento, on_delete=models.CASCADE, related_name='funcionarios')

    def _calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def clean(self):
        super().clean()
        if self.fecha_nacimiento:
            edad = self._calcular_edad()
            if edad < 18:
                raise ValidationError({
                    'fecha_nacimiento': 'El funcionario debe tener al menos 18 anos.'
                })

    def save(self, *args, **kwargs):
        if self.fecha_nacimiento:
            self.edad = self._calcular_edad()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"
    
    
class FuncionarioSome(models.Model):
    nombres = models.CharField(max_length=200)
    apellido_paterno = models.CharField(max_length=100, null=True, blank=True)
    apellido_materno = models.CharField(max_length=100 , null=True, blank=True)
    # Creamos la regla: 7 a 8 números, un guion, y un número o la letra 'K' al final
    validador_rut = RegexValidator(
        regex=r'^\d{7,8}-[\dkK]$', 
        message='El RUT debe tener el formato 12345678-9 (sin puntos y con guion).'
    )
    rut = models.CharField(
        max_length=20, 
        unique=True, 
        validators=[validador_rut],
        null=True, # Déjalo si elegiste la opción 2 del paso anterior
        blank=True
    )
    genero = models.CharField(max_length=50)
    edad = models.PositiveSmallIntegerField(null=True, blank=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=50)
    ciudad_pueblo_localidad = models.CharField(max_length=100)
    comuna = models.CharField(max_length=100)
    provincia = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    profesion = models.CharField(max_length=100)
    universidad = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_conexion = models.DateTimeField(auto_now=True)
    red = models.ForeignKey(RedHospitalaria, on_delete=models.CASCADE, null=True, blank=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='funcionarios_some', null=True, blank=True)

    def _calcular_edad(self):
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def clean(self):
        super().clean()
        if self.fecha_nacimiento:
            edad = self._calcular_edad()
            if edad < 18:
                raise ValidationError({
                    'fecha_nacimiento': 'El funcionario debe tener al menos 18 anos.'
                })

    def save(self, *args, **kwargs):
        if self.fecha_nacimiento:
            self.edad = self._calcular_edad()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.nombres} {self.apellido_paterno} {self.apellido_materno}"

class Box(models.Model):
    nombre_box = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    profesional_asignado = models.CharField(max_length=100)
    esta_ocupado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    registros_uso = models.DateTimeField(null=True, blank=True)
    fecha_ultimo_uso = models.DateTimeField(null=True, blank=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='boxes')
    profesionales = models.ManyToManyField(Profesional, related_name='boxes_asignados')

    def __str__(self):
        return self.nombre_box
    
class Reserva(models.Model):
    motivo_consulta = models.CharField(max_length=100)
    nombre_paciente = models.CharField(max_length=200)
    genero_paciente = models.CharField(max_length=50)
    edad_paciente = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    programa_salud = models.CharField(max_length=100)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='reservas')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='reservas_atendidas')
    funcionario_some = models.ForeignKey(FuncionarioSome, on_delete=models.CASCADE, related_name='reservas_creadas', null=True, blank=True)
    box = models.ForeignKey(Box, on_delete=models.CASCADE, related_name='reservas', null=True, blank=True)
    tipo_consulta = models.CharField(max_length=100, null=True, blank=True)
    fecha_hora = models.DateTimeField(null=True, blank=True)
    tipo_atencion = models.CharField(max_length=100, null=True, blank=True)
    duracion_cita = models.CharField(max_length=50, null=True, blank=True)
    confirma_asistencia = models.BooleanField(default=False)
    reprograma_cita = models.BooleanField(default=False)
    cancela_cita = models.BooleanField(default=False)
    motivo_cancelacion = models.CharField(max_length=200, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_paciente} - {self.motivo_consulta}"


class Registro(models.Model):
    motivo_consulta = models.CharField(max_length=100)
    nombre_paciente = models.CharField(max_length=200)
    genero_paciente = models.CharField(max_length=50)
    edad_paciente = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    programa_salud = models.CharField(max_length=100)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='registros')
    profesional = models.ForeignKey(Profesional, on_delete=models.CASCADE, related_name='registros_atendidos')

    def __str__(self):
        return f"{self.nombre_paciente} - {self.motivo_consulta}"


