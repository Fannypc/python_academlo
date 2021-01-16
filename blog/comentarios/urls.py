from rest_framework.routers import DefaultRouter

from comentarios.views import ComentarioViewSet

router = DefaultRouter()
router.register(r'', ComentarioViewSet)

urlpatterns = router.urls
