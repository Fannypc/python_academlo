from rest_framework.routers import DefaultRouter

from editoriales.views import EditorialViewSet

router = DefaultRouter()
router.register(r'', EditorialViewSet)

urlpatterns = router.urls
