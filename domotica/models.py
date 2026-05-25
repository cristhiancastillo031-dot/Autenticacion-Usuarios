# domotica/models.py
from django.db import models
from django.conf import settings # Para traer tu Custom User Model de forma segura

class Casa(models.Model):
    # Una casa le pertenece a un único usuario (tu modelo personalizado)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='casas')
    nombre = models.CharField(max_length=100, help_text="Ej: Casa de la Playa, Mi Departamento")
    direccion = models.CharField(max_length=200, blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} ({self.usuario.email})"


class Habitacion(models.Model):
    # Una habitación pertenece a una sola casa. Si la casa se borra, sus habitaciones también (CASCADE)
    casa = models.ForeignKey(Casa, on_delete=models.CASCADE, related_name='habitaciones')
    nombre = models.CharField(max_length=100, help_text="Ej: Sala Principal, Dormitorio, Cocina")
    
    def __str__(self):
        return f"{self.nombre} - {self.casa.nombre}"


class Dispositivo(models.Model):
    # Tipos de dispositivos permitidos
    TIPOS_DISPOSITIVOS = [
        ('LUZ', 'Iluminación'),
        ('TV', 'Televisor / Entretenimiento'),
        ('AC', 'Aire Acondicionado'),
        ('CAM', 'Cámara de Seguridad'),
    ]

    # Un dispositivo está dentro de una habitación específica
    habitacion = models.ForeignKey(Habitacion, on_delete=models.CASCADE, related_name='dispositivos')
    nombre = models.CharField(max_length=100, help_text="Ej: Foco Inteligente 1, Smart TV")
    tipo = models.CharField(max_length=10, choices=TIPOS_DISPOSITIVOS, default='LUZ')
    
    # Lógica elemental del estado del dispositivo
    esta_encendido = models.BooleanField(default=False)
    valor_ajuste = models.IntegerField(default=0, help_text="Para la intensidad de la luz (0-100) o temperatura del AC")

    def __str__(self):
        return f"{self.nombre} ({self.get_tipo_display()}) en {self.habitacion.nombre}"

