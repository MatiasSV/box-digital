from django.contrib import admin
from .models import RedHospitalaria, Establecimiento, Estamento, Profesional, Box, Registro, FuncionarioSome, Reserva

# Register your models here.
admin.site.register(RedHospitalaria)
admin.site.register(Establecimiento)
admin.site.register(Estamento)
@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    readonly_fields = ("edad",)

    class Media:
        js = ('someApp/js/chained_dropdowns.js',)

@admin.register(FuncionarioSome)
class FuncionarioSomeAdmin(admin.ModelAdmin):
    readonly_fields = ("edad",)

admin.site.register(Box)
admin.site.register(Registro)
admin.site.register(Reserva)
