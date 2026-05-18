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

class Funcionario(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.CharField(max_length=20, unique=True)
    genero = models.CharField(max_length=50)
    edad = models.CharField(max_length=10)
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
    email = models.EmailField(max_length=100)
    contrasena = models.CharField(max_length=255)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    ultima_conexion = models.DateTimeField(auto_now=True)
    red = models.ForeignKey(RedHospitalaria, on_delete=models.CASCADE, null=True, blank=True)
    estamento = models.ForeignKey(Estamento, on_delete=models.CASCADE, related_name='funcionarios')

    def __str__(self):
        return self.nombre

class Box(models.Model):
    nombre_box = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    profesional_asignado = models.CharField(max_length=100)
    esta_ocupado = models.BooleanField(default=False)
    fecha_creacion = models.DateField(auto_now_add=True)
    registros_uso = models.DateTimeField(null=True, blank=True)
    fecha_ultimo_uso = models.DateTimeField(null=True, blank=True)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='boxes')
    funcionarios = models.ManyToManyField(Funcionario, related_name='boxes_asignados')

    def __str__(self):
        return self.nombre_box

class Registro(models.Model):
    motivo_consulta = models.CharField(max_length=100)
    nombre_paciente = models.CharField(max_length=200)
    genero_paciente = models.CharField(max_length=50)
    edad_paciente = models.CharField(max_length=10)
    comuna = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    programa_salud = models.CharField(max_length=100)
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.CASCADE, related_name='registros')
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, related_name='registros_atendidos')

    def __str__(self):
        return f"{self.nombre_paciente} - {self.motivo_consulta}"
