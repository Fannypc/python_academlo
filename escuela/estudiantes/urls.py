from django.urls import path

from estudiantes.views import get_estudiantes, get_estudiante

app_name = 'estudiantes'
urlpatterns = [
    path('', get_estudiantes, name='list'),
    path('<estudiante_id>/', get_estudiante, name='detail')
]
