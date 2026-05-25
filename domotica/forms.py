# domotica/forms.py
from django import forms
from .models import Casa
from .models import Habitacion, Dispositivo


class CasaForm(forms.ModelForm):
    class Meta:
        model = Casa
        # Solo le pedimos al usuario el nombre y la dirección
        # Ocultamos el campo 'usuario' porque lo asignaremos automáticamente en el backend por seguridad
        fields = ['nombre', 'direccion']
        
        # Agregamos estilos de Tailwind CSS directamente a los inputs
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Ej: Casa de la Playa, Mi Departamento'
            }),
            'direccion': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500',
                'placeholder': 'Ej: Av. Principal 123'
            }),
        }

class HabitacionForm(forms.ModelForm):
    class Meta:
        model = Habitacion
        fields = ['nombre'] # Ocultamos 'casa' para asignarla dinámicamente
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none',
                'placeholder': 'Ej: Dormitorio, Cocina'
            }),
        }

class DispositivoForm(forms.ModelForm):
    class Meta:
        model = Dispositivo
        fields = ['nombre', 'tipo'] # Ocultamos 'habitacion' e 'esta_encendido'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'w-full p-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none',
                'placeholder': 'Ej: Foco Inteligente'
            }),
            'tipo': forms.Select(attrs={
                'class': 'w-full p-2 text-sm border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none bg-white'
            }),
        }
