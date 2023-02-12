from rest_framework.routers import DefaultRouter

from .views import EventViews

router = DefaultRouter()
router.register("events", EventViews)
urlpatterns = router.urls
