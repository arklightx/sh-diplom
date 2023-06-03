from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        exclude = ["permissions"]

    
class HomeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    street = serializers.CharField()
    home_number = serializers.CharField()
    microdistrict = serializers.CharField()
    area = serializers.FloatField()
    create_dt = serializers.DateTimeField()
    is_deleted = serializers.BooleanField()
    jitsi = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    homes = HomeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "groups", "phone", "patronymic", "homes"]


class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class AuthRespSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=2048)
    user = UserSerializer()
