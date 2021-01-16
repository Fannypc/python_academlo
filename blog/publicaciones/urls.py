from rest_framework.routers import DefaultRouter

from publicaciones.views import PublicacionViewSet

router = DefaultRouter()
router.register(r'', PublicacionViewSet)

urlpatterns = router.urls
