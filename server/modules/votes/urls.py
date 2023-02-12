from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import VotesViews, VotesVariantsViews, CreateVoteView

router = DefaultRouter()
router.register("votes", VotesViews)
router.register("votes-variants", VotesVariantsViews)
urlpatterns = [
    path("createvote/", CreateVoteView.as_view())
] + router.urls
