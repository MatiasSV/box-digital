from rest_framework import permissions
from .models import FuncionarioSome, Profesional

def is_funcionario(user):
    if not user.is_authenticated:
        return False
    return user.is_superuser or FuncionarioSome.objects.filter(email=user.email).exists()

def is_profesional(user):
    if not user.is_authenticated:
        return False
    return user.is_superuser or Profesional.objects.filter(email=user.email).exists()

class IsFuncionarioSome(permissions.BasePermission):
    """
    Permite acceso solo a funcionarios SOME.
    """
    def has_permission(self, request, view):
        return is_funcionario(request.user)

class IsProfesional(permissions.BasePermission):
    """
    Permite acceso solo a Profesionales de la salud.
    """
    def has_permission(self, request, view):
        return is_profesional(request.user)

class IsProfesionalOrFuncionario(permissions.BasePermission):
    """
    Permite acceso si es profesional o funcionario.
    """
    def has_permission(self, request, view):
        return is_profesional(request.user) or is_funcionario(request.user)
