from django.contrib.auth.hashers import check_password
from rest_framework import permissions, status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import CreateAPIView, DestroyAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.exception import ClientException

from .auth import AuthenticationSystem, generate_jwt_pair, decode_jwt
from .models import User, AccessTokens, RefreshTokens
from .serializers import AuthorizationSerializer, AuthRespSerializer, UserSerializer

import datetime
from django.conf import settings


class Authorization(CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AuthorizationSerializer
    authentication_classes = []

    def post(self, request, *args, **kwargs):
        data = request.data
        try:
            candidate = User.objects.get(username=data.get("username"))
        except Exception as e:
            raise ClientException("Неверный логин или пароль", status.HTTP_400_BAD_REQUEST)
        if check_password(data.get("password"), candidate.password):
            pair = generate_jwt_pair(candidate)
            response_data = {
                "access": pair.access.token,
                "user": candidate
            }
            response_cookie = {
                "key": "refresh",
                "value": pair.refresh.token,
                "httponly": True,
                "expires": settings.JWT_REFRESH_LIFETIME + datetime.datetime.now(),
                "samesite": "Lax"
            }
            response = Response(AuthRespSerializer(response_data).data, status=status.HTTP_200_OK)
            response.set_cookie(**response_cookie)
            return response
        raise ClientException("Неверный логин или пароль", status.HTTP_400_BAD_REQUEST)


class Logout(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [AuthenticationSystem]

    def delete(self, request: Request, *args, **kwargs):
        AccessTokens.objects.get(token=request.auth.token).delete()
        response = Response(status=status.HTTP_204_NO_CONTENT)
        ck = {
            "key": "refresh",
            "value": "",
            "httponly": True,
            "expires": settings.JWT_REFRESH_LIFETIME + datetime.datetime.now(),
            "samesite": "Lax"
        }
        response.set_cookie(**ck)
        return response

class NewTokenPair(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request: Request, *args, **kwargs):
        token = request.COOKIES.get("refresh")
        if token is None or token == '':
            raise ClientException("Необходимо перезайти", status.HTTP_400_BAD_REQUEST)
        decoded_token = decode_jwt(token)
        if not decoded_token.is_valid:
            raise ClientException("Необходимо перезайти", status.HTTP_401_UNAUTHORIZED)
        refresh_model = RefreshTokens.objects.get(token=decoded_token.token)
        new_pair = generate_jwt_pair(refresh_model.user)
        AccessTokens.objects.get(token=refresh_model.access.token).delete()
        response = Response({"access": new_pair.access.token}, status=status.HTTP_200_OK)
        ck = {
            "key": "refresh",
            "value": new_pair.refresh.token,
            "httponly": True,
            "expires": settings.JWT_REFRESH_LIFETIME + datetime.datetime.now(),
            "samesite": "Lax"
        }
        response.set_cookie(**ck)
        return response


class CheckTokenView(APIView):
    permission_classes = [permissions.AllowAny]
    authentication_classes = []

    def post(self, request: Request, *args, **kwargs):
        token = request.COOKIES.get("refresh")
        try:
            RefreshTokens.objects.get(token=token)
        except:
            return Response("0")
        return Response("1")

class UserChangeView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request: Request, *args, **kwargs):
        fields = ["first_name", "last_name", "phone", "email", "patronymic"]
        changed_data = {}
        for item in fields:
            if item in request.data:
                value = request.data.get(item)
                setattr(request.user, item, value)
                changed_data[item] = value
        request.user.save()
        return Response(changed_data, status=200)


class UserView(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer
