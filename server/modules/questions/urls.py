from rest_framework.routers import DefaultRouter
from .views import QuestionView

router = DefaultRouter()
router.register("questions", QuestionView)

urlpatterns = router.urls
