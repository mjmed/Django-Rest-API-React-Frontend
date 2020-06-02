from rest_framework import routers
from .views import AnestesiaViewSet

router = routers.DefaultRouter()
router.register('api/anestesias', AnestesiaViewSet, 'anestesias')

urlpatterns = router.urls
