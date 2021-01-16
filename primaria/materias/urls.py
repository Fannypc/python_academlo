from django.urls import path

from materias.views import MateriaList, MateriaDetail

app_name = 'materias'
urlpatterns = [
    path('', MateriaList.as_view(), name='list'),
    path('<materia_id>/', MateriaDetail.as_view(), name='detail')
]