from rest_framework.routers import DefaultRouter
from .views import UserView, UserChangeView
from django.urls import path

router = DefaultRouter()
router.register("users", UserView)

urlpatterns = router.urls
urlpatterns += [
    path("users/change/private_data/", UserChangeView.as_view()),
]
