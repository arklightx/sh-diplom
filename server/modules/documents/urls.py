from rest_framework.routers import DefaultRouter
from .views import DocumentView, DisablingsView

router = DefaultRouter()
router.register("documents", DocumentView)
router.register("disablings", DisablingsView)
urlpatterns = router.urls