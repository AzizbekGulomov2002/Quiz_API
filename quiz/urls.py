from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FanlarViewSet, SavolBodyViewSet, SavolDarajasiViewSet

router = DefaultRouter()
router.register('fanlar', FanlarViewSet)
router.register('savollar', SavolBodyViewSet)
router.register('savol-darajalari', SavolDarajasiViewSet)


urlpatterns = [
    path("", include(router.urls))
]
