from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from modules.home.models import Home, HomeLevel, Apartment, Staff
from modules.home.serializers import HomeSerializer, HomeLevelSerializer, ApartmentSerializer, StaffSerializer


class HomeView(ReadOnlyModelViewSet):
    queryset = Home.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HomeSerializer
    authentication_classes = []


class HomeLevelView(ReadOnlyModelViewSet):
    queryset = HomeLevel.objects.all()
    permission_classes = [AllowAny]
    serializer_class = HomeLevelSerializer
    authentication_classes = []


class ApartmentView(ReadOnlyModelViewSet):
    queryset = Apartment.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ApartmentSerializer
    authentication_classes = []


class StaffView(ReadOnlyModelViewSet):
    queryset = Staff.objects.all()
    permission_classes = [AllowAny]
    serializer_class = StaffSerializer
    authentication_classes = []
