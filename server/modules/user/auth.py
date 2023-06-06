from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from datetime import datetime
import jwt
from django.conf import settings
from modules.exception import ClientException

from .models import User, AccessTokens, RefreshTokens

class BaseToken:
    token: str | None
    payload: dict
    is_valid: bool
    exp_delta: datetime.time

    def __init__(self, token: str, payload: dict):
        self.token = token
        self.payload = payload
        self.is_valid = False


class AccessToken(BaseToken):
    exp_delta = settings.JWT_ACCESS_LIFETIME


class RefreshToken(BaseToken):
    exp_delta = settings.JWT_REFRESH_LIFETIME


class JWTPair:
    __access: AccessToken | None
    __refresh: RefreshToken | None

    def __init__(self, access: AccessToken = None, refresh: RefreshToken = None):
        self.__access = access
        self.__refresh = refresh

    @property
    def access(self) -> AccessToken:
        return self.__access

    @access.setter
    def access(self, access: AccessToken):
        self.__access = access

    @property
    def refresh(self) -> RefreshToken:
        return self.__refresh

    @refresh.setter
    def refresh(self, refresh: RefreshToken):
        self.__refresh = refresh

    def to_dict(self):
        return {"access": self.__access, "refresh": self.__refresh}


def encode_jwt(payload: dict, t_type: str) -> AccessToken | RefreshToken:
    if t_type == "a":
        payload["exp_time"] = str(datetime.now() + settings.JWT_ACCESS_LIFETIME)
        payload["t_type"] = "a"
    else:
        payload["exp_time"] = str(datetime.now() + settings.JWT_REFRESH_LIFETIME)
        payload["t_type"] = "r"
    token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
    encoded_token = AccessToken(token, payload) if payload["t_type"] == "a" else RefreshToken(token, payload)
    encoded_token.is_valid = True
    return encoded_token


def decode_jwt(token: str) -> AccessToken | RefreshToken:
    info = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"], options={"verify_signature": True})
    decoded_token = AccessToken(token, info) if info.get("t_type") == "a" else RefreshToken(token, info)
    decoded_token.is_valid = datetime.strptime(info.get("exp_time"), "%Y-%m-%d %H:%M:%S.%f") > datetime.now()
    return decoded_token


def generate_jwt_pair(user: User) -> JWTPair:
    access_info = {"id": user.id}
    refresh_info = {"id": user.id}

    access_token = encode_jwt(access_info, "a")
    refresh_token = encode_jwt(refresh_info, "r")
    acc_token_model = AccessTokens.objects.create(token=access_token.token,
                                                  user_id=user.id,
                                                  valid_to=(datetime.now() + access_token.exp_delta))
    RefreshTokens.objects.create(token=refresh_token.token,
                                 user_id=user.id,
                                 valid_to=(datetime.now() + refresh_token.exp_delta),
                                 access_id=acc_token_model.token)
    return JWTPair(access_token, refresh_token)


class AuthenticationSystem(BaseAuthentication):
    def authenticate(self, request: Request, *args, **kwargs):
        try:
            header = request.headers.get("Authorization")
            if header is None:
                return None
            header_token = header.split(" ")[1]
            encoded_token = decode_jwt(header_token)
            if not encoded_token.is_valid:
                return None
        except Exception as e:
            return None
        if isinstance(encoded_token, AccessToken):
            try:
                user_id = encoded_token.payload.get("id")
                candidate = User.objects.get(id=user_id)
                AccessTokens.objects.get(token=encoded_token.token)
                return candidate, encoded_token
            except Exception as e:
                return None
        raise ClientException("Ошибка аутентификации", 400)
