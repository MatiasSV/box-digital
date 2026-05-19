from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'redes-hospitalarias', views.RedHospitalariaViewSet)
router.register(r'establecimientos', views.EstablecimientoViewSet)
router.register(r'estamentos', views.EstamentoViewSet)
router.register(r'profesionales', views.ProfesionalViewSet)
router.register(r'boxes', views.BoxViewSet)
router.register(r'registros', views.RegistroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]