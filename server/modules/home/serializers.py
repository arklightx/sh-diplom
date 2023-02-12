from rest_framework import serializers

from .models import Home, HomeLevel, Apartment
from ..user.serializers import UserSerializer


class HomeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Home
        fields = "__all__"


class HomeLevelSerializer(serializers.ModelSerializer):
    home = HomeSerializer(many=False, read_only=True)

    class Meta:
        model = HomeLevel
        fields = "__all__"


class ApartmentSerializer(serializers.ModelSerializer):
    level = HomeLevelSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)

    class Meta:
        model = Apartment
        fields = "__all__"
