from django.shortcuts import render
from django.http import HttpResponse
from estudiantes.models import Estudiante


def get_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'estudiantes/lista.html', {'estudiantes': estudiantes})


def get_estudiante(request, estudiante_id):
    estudiante = Estudiante.objects.get(id=estudiante_id)
    # enviar un 404 cuando no existe el registro:
    # estudiante = get_object_or_404(Estudiante, id=estudiante_id)
    return render(request, 'estudiantes/detalle.html', {'estudiante': estudiante})
