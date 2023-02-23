import uuid

from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group
from rest_framework import serializers

from core.email import send_email_template
from core.exception import ServerException
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


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True, read_only=True)
    homes = HomeSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email", "groups", "phone", "patronymic", "homes"]


class RegistrationSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        group = Group.objects.get(name="user")
        group.user_set.add(user)
        email_token = uuid.uuid4().hex
        user.token_email = email_token
        user.save()
        send_email_template([user.email],
                            "Подтверждение адреса электронной почты",
                            "email_confirm.html",
                            {
                                "link": f"{settings.BASE_PROTOCOL}://{settings.BASE_DOMAIN}{settings.BASE_PORT}/auth/confirm/?token={email_token}"})
        return user

    class Meta:
        model = User
        fields = ["username", "password", "email"]


class AuthorizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password"]


class ConfirmRegistrationSerializer(serializers.ModelSerializer):

    def update(self, instance, validated_data):
        instance.token_email = None
        instance.is_active = True
        instance.is_confirmed_email = True
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ["token_email"]


class PasswordChangeSerializer(serializers.Serializer):
    email = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        token = uuid.uuid4().hex
        instance.token_password_change = token
        instance.save()
        send_email_template(
            [validated_data.get("email")],
            "Восстановление пароля",
            "password_forgot.html",
            {
                "link": f"{settings.BASE_PROTOCOL}://{settings.BASE_DOMAIN}{settings.BASE_PORT}/auth/recovery/?token={token}"
            }
        )
        return instance


class ConfirmPasswordChangeSerializer(serializers.Serializer):
    token = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        raise ServerException()

    def update(self, instance, validated_data):
        instance.token_password_change = None
        instance.password = make_password(validated_data.get("password"))
        instance.save()
        return instance


class AuthRespSerializer(serializers.Serializer):
    access = serializers.CharField(max_length=2048)
    user = UserSerializer()
