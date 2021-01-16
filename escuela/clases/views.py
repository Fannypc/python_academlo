from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

from clases.models import Clase


def get_clase(request, clase_id):
    clase = Clase.objects.get(id=clase_id)
    estudiantes = clase.estudiantes.all()
    return render(request, 'clases/detalle.html', {'clase': clase, 'estudiantes': estudiantes})


class ClaseView(View):
    http_method_names = ['get']
    template_name = 'clases/lista.html'

    def get(self, request):
        clases = Clase.objects.all()
        context = {
            'clases': clases
        }
        return render(
            request,
            self.template_name,
            context=context
        )
