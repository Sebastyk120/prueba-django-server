import os
import tempfile
import io
import json
from datetime import datetime
from django.contrib import messages
from django.contrib.admin.views.decorators import user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.db import IntegrityError, transaction
from django.core.management import call_command
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View


# Create your views here.

class MigrateView(LoginRequiredMixin, UserPassesTestMixin, View):
    def test_func(self):
        # Solo permitir acceso a usuarios que son administradores
        return self.request.user.is_superuser

    def get(self, request, *args, **kwargs):
        try:
            with transaction.atomic():
                # Ejecutar 'makemigrations' para todas las aplicaciones
                call_command('makemigrations')

                # Ejecutar 'migrate' para todas las aplicaciones
                call_command('migrate')

            return HttpResponse("Todas las migraciones realizadas con éxito.")
        except Exception as e:
            # Capturar cualquier error que pueda ocurrir durante la ejecución de las migraciones
            return HttpResponse(f"Error al realizar las migraciones: {str(e)}", status=500)


def home(request):
    return render(request, 'home.html')


def login1(request):
    if request.method == 'GET':
        return render(request, 'login2.html', {'form': AuthenticationForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            messages.error(request, f'Usuario o contraseña incorrecto')
            return render(request, 'login2.html',
                          {'form': AuthenticationForm})
        else:
            login(request, user)
            return redirect('home')


@user_passes_test(lambda u: User.objects.count() == 0, login_url='/login/')
def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                # Registrar usuario.
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.is_superuser = True
                user.is_staff = True
                user.save()
                messages.success(request, "Superusuario creado correctamente")
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm, "error": 'El usuario ya existe'})
        return render(request, 'signup.html', {'form': UserCreationForm, "error": 'Las contraseñas no coinciden'})


@login_required
def salir(request):
    logout(request)
    return redirect('home')


class CustomPasswordResetView(PasswordResetView):
    title = 'Restablecer Contraseña - Heavens Fruits'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_name'] = "Administración Heavens Fruits"
        return context


class BackupDataView(View):
    def get(self, request, *args, **kwargs):
        # Renderizar la plantilla con el botón para descargar
        return render(request, 'backup.html')

    def post(self, request, *args, **kwargs):
        # Crear un archivo temporal para almacenar el backup
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            try:
                # Usar StringIO para capturar la salida de dumpdata
                output = io.StringIO()
                # Obtener la lista de todos los modelos en la aplicación
                from django.apps import apps
                models = apps.get_models()
                # Construir la lista de modelos a excluir que contienen "historical"
                exclude_models = [model._meta.label_lower for model in models if
                                  'historical' in model._meta.label_lower]
                # Excluir los modelos históricos durante la exportación
                call_command('dumpdata', exclude=exclude_models, stdout=output)
                temp_file.write(output.getvalue().encode('utf-8'))
                temp_file_name = temp_file.name
            except Exception as e:
                return HttpResponse(f'Error during backup: {e}', content_type='text/plain')

        # Obtener la fecha y hora actual para incluirla en el nombre del archivo
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"copia_heavens_{current_time}.json"

        # Leer el contenido del archivo temporal
        with open(temp_file_name, 'rb') as backup_file:
            response = HttpResponse(backup_file.read(), content_type='application/json')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'

        # Eliminar el archivo temporal después de la respuesta
        os.remove(temp_file_name)
        return response


class RestoreDataView(View):
    def post(self, request, *args, **kwargs):
        if 'backup_file' not in request.FILES:
            return HttpResponse('No file uploaded', content_type='text/plain')

        backup_file = request.FILES['backup_file']

        # Guardar el archivo temporalmente
        with tempfile.NamedTemporaryFile(delete=False, suffix='.json') as temp_file:
            for chunk in backup_file.chunks():
                temp_file.write(chunk)
            temp_file_name = temp_file.name

        # Leer el contenido del archivo temporal
        try:
            with open(temp_file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)

            # Restaurar los datos usando loaddata
            call_command('loaddata', temp_file_name)
            os.remove(temp_file_name)
            return HttpResponse('Data restored successfully', content_type='text/plain')
        except Exception as e:
            os.remove(temp_file_name)
            return HttpResponse(f'Error during data restoration: {e}', content_type='text/plain')
