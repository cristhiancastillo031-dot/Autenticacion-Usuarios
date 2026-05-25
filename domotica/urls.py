# domotica/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('mis-casas/', views.listar_casas, name='mis_casas'),
]
