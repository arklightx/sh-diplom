from rest_framework.routers import DefaultRouter

from .views import RequestsView

router = DefaultRouter()
router.register("requests", RequestsView)

urlpatterns = router.urls
