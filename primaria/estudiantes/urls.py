from django.urls import path

from estudiantes.views import EstudianteList, EstudianteDetail

app_name = 'estudiantes'
urlpatterns = [
    path('', EstudianteList.as_view(), name='list'),
    path('<estudiante_id>/', EstudianteDetail.as_view(), name='detail')
]