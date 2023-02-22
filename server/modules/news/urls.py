from rest_framework import routers
from .views import NewsViewSet

router = routers.DefaultRouter()
router.register("news", NewsViewSet)
urlpatterns = router.urls

