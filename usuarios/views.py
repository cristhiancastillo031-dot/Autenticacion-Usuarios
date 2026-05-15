from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'¡Cuenta creada con éxito para {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'usuarios/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Django extrae el valor del input del formulario (que se llama 'username' en el HTML)
            correo_o_usuario = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')
            
            # Pasamos 'username' al authenticate porque Django internamente mapea tu USERNAME_FIELD aquí
            user = authenticate(username=correo_o_usuario, password=password)
            
            if user is not None:
                auth_login(request, user)
                messages.success(request, f'¡Bienvenido de nuevo!')
                return redirect('dashboard')
        else:
            # IMPRESIÓN DE DEBUG: Si el formulario falla, esto te dirá por qué en la consola de comandos
            print("Errores del formulario:", form.errors) 
    else:
        form = AuthenticationForm()
        
    return render(request, 'usuarios/login.html', {'form': form})


@login_required(login_url='login')  # Si no está logueado, lo manda a la pantalla de login
def dashboard(request):
    # Aquí puedes pasar los datos del usuario actual al HTML
    contexto = {
        'usuario': request.user,
    }
    return render(request, 'usuarios/dashboard.html', contexto)
