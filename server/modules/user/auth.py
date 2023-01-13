from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request

from src.core.exception import ClientException
from src.core.security import jwt
from src.core.security.jwt import AccessToken

from .models import User, AccessTokens


class AuthenticationSystem(BaseAuthentication):
    def authenticate(self, request: Request, *args, **kwargs):
        try:
            header = request.headers.get("Authorization")
            if header is None:
                return None
            header_token = header.split(" ")[1]
            encoded_token = jwt.decode_jwt(header_token)
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
