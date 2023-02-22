from rest_framework.routers import DefaultRouter

from modules.home.views import HomeView, HomeLevelView, ApartmentView, StaffView

router = DefaultRouter()
router.register("homes", HomeView)
router.register("levels", HomeLevelView)
router.register("apartments", ApartmentView)
router.register("staffs", StaffView)
urlpatterns = router.urls
