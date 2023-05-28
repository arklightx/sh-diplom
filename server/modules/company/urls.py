from .views import CompanyViewSet, CompanyServicesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register("company", CompanyViewSet)
router.register("company_services", CompanyServicesViewSet)
urlpatterns = router.urls
