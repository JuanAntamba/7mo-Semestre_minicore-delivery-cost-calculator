from django.urls import path
from . import views

urlpatterns = [
    # Esta será la ruta principal de la mini-aplicación
    path('', views.calcular_reporte_costos, name='reporte_costos'),
]