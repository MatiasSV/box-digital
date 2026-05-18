from django.contrib import admin
from .models import RedHospitalaria, Establecimiento, Estamento, Funcionario, Box, Registro

# Register your models here.
admin.site.register(RedHospitalaria)
admin.site.register(Establecimiento)
admin.site.register(Estamento)
admin.site.register(Funcionario)
admin.site.register(Box)
admin.site.register(Registro)
