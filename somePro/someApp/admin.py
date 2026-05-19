from django.contrib import admin
from .models import RedHospitalaria, Establecimiento, Estamento, Funcionario, Box, Registro

# Register your models here.
admin.site.register(RedHospitalaria)
admin.site.register(Establecimiento)
admin.site.register(Estamento)
@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
	readonly_fields = ("edad",)
admin.site.register(Box)
admin.site.register(Registro)
