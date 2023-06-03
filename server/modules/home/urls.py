from rest_framework.routers import DefaultRouter

from modules.home.views import HomeView, HomeLevelView, ApartmentView, StaffView, StaffFeedbackView

router = DefaultRouter()
router.register("homes", HomeView)
router.register("levels", HomeLevelView)
router.register("apartments", ApartmentView)
router.register("staffs", StaffView)
router.register("staff_feedback", StaffFeedbackView)
urlpatterns = router.urls
