from django.urls import path

from clases.views import get_clase, ClaseView

app_name = 'clases'
urlpatterns = [
    #path('', get_clases, name='list'),
    path('view/', ClaseView.as_view(), name='list'),
    path('<clase_id>/', get_clase, name='detail')
]
