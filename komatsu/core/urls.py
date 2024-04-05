# core/urls.py

from django.urls import path
from .views import os_list, update_os_estado_trabajo, actualizar_os, detalle_os, actualizar_os, actualizar_estado_trabajo

urlpatterns = [
    path('os-list/', os_list, name='os_list'),
    path('update_os_estado_trabajo/', update_os_estado_trabajo, name='update_os_estado_trabajo'),
    # Otras URLs de tu aplicación
    path('detalle_os/<int:os_id>/', detalle_os, name='detalle_os'),
    path('actualizar_os/', actualizar_os, name='actualizar_os'),
    path('actualizar_estado_trabajo/', actualizar_estado_trabajo, name='actualizar_estado_trabajo'),
]