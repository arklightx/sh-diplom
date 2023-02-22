from rest_framework import serializers

from .models import Home, HomeLevel, Apartment, Staff
from ..user.serializers import UserSerializer
from modules.documents.serializers import DisablingsSerializer, DocumentSerializer
from modules.events.serializers import EventSerializer
from modules.reqs_to_company.serializers import RequestsSerializer


class StaffSerializer(serializers.ModelSerializer):

    class Meta:
        model = Staff
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, read_only=True)
    disablings = DisablingsSerializer(many=True, read_only=True)

    class Meta:
        model = Apartment
        fields = "__all__"


class HomeLevelSerializer(serializers.ModelSerializer):
    apartments = ApartmentSerializer(many=True, read_only=True)
    class Meta:
        model = HomeLevel
        fields = "__all__"


class HomeSerializer(serializers.ModelSerializer):
    documents = DocumentSerializer(many=True, read_only=True)
    levels = HomeLevelSerializer(many=True, read_only=True)
    staffs = StaffSerializer(many=True, read_only=True)
    events = EventSerializer(many=True, read_only=True)
    requests = RequestsSerializer(many=True, read_only=True)
    class Meta:
        model = Home
        fields = "__all__"
