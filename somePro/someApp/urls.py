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
router.register(r'funcionarios-some', views.FuncionarioSomeViewSet)
router.register(r'reservas', views.ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('ajax/load-establecimientos/', views.get_establecimientos, name='ajax_load_establecimientos'),
    path('ajax/load-estamentos/', views.get_estamentos, name='ajax_load_estamentos'),
]