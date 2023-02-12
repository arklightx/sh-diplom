from rest_framework.routers import DefaultRouter

from modules.home.views import HomeView, HomeLevelView, ApartmentView

router = DefaultRouter()
router.register("homes", HomeView)
router.register("levels", HomeLevelView)
router.register("apartments", ApartmentView)
urlpatterns = router.urls
