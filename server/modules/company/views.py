from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import CompanySerializer, CompanyServicesSerializer
from .models import Company, CompanyServices
from rest_framework.permissions import AllowAny


class CompanyViewSet(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]


class CompanyServicesViewSet(ReadOnlyModelViewSet):
    queryset = CompanyServices.objects.all()
    serializer_class = CompanyServicesSerializer
    permission_classes = [AllowAny]
