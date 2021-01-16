from django.urls import path

from profesores.views import ProfesorList, ProfesorDetail

app_name = 'profesores'
urlpatterns = [
    path('', ProfesorList.as_view(), name='list'),
    path('<profesor_id>/', ProfesorDetail.as_view(), name='detail')
]