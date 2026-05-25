# domotica/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Casa, Habitacion
from .forms import CasaForm, HabitacionForm, DispositivoForm

@login_required(login_url='login')
def listar_casas(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        # PROCESAR NUEVA CASA
        if action == 'guardar_casa':
            form_casa = CasaForm(request.POST)
            if form_casa.is_valid():
                nueva_casa = form_casa.save(commit=False)
                nueva_casa.usuario = request.user
                nueva_casa.save()
                return redirect('mis_casas')
                
        # PROCESAR NUEVA HABITACIÓN
        elif action == 'guardar_habitacion':
            form_hab = HabitacionForm(request.POST)
            casa_id = request.POST.get('casa_id')
            casa = get_object_or_404(Casa, id=casa_id, usuario=request.user)
            if form_hab.is_valid():
                nueva_hab = form_hab.save(commit=False)
                nueva_hab.casa = casa
                nueva_hab.save()
                return redirect('mis_casas')
                
        # PROCESAR NUEVO DISPOSITIVO
        elif action == 'guardar_dispositivo':
            form_disp = DispositivoForm(request.POST)
            hab_id = request.POST.get('habitacion_id')
            # Aseguramos que la habitación pertenezca a una casa del usuario actual
            habitacion = get_object_or_404(Habitacion, id=hab_id, casa__usuario=request.user)
            if form_disp.is_valid():
                nuevo_disp = form_disp.save(commit=False)
                nuevo_disp.habitacion = habitacion
                nuevo_disp.save()
                return redirect('mis_casas')

    # Si entramos por GET, pasamos los tres formularios en blanco al contexto con los nombres correctos
    contexto = {
        'casas': request.user.casas.all(),
        'casa_form': CasaForm(),
        'habitacion_form': HabitacionForm(),
        'dispositivo_form': DispositivoForm(),
    }
    return render(request, 'domotica/mis_casas.html', contexto)
