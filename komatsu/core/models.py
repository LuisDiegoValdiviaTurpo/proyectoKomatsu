# core/models.py
from django.db import models

class OS(models.Model):
    estado_choices = [
        ('TODO', 'To-Do'),
        ('IN_PROCESS', 'In-Process'),
        ('DONE', 'Done'),
    ]
    estado = models.CharField(max_length=20, choices=estado_choices, default='TODO')
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    estado_trabajo = models.CharField(max_length=20, choices=[('ARMADO', 'Armado'), ('DESARME', 'Desarme')], default='DESARME')
