from datetime import timedelta, timezone, datetime

import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User


def generate_new_token_pair(user):
    refresh = RefreshToken.for_user(user)
    access = refresh.access_token
    return str(access), str(refresh)


def get_token(email: str, user_id: int) -> str:
    token = jwt.encode(payload={"email": email, "id": user_id,
                                "exp": datetime.now(timezone(timedelta(hours=4))) + timedelta(hours=1)},
                       key=settings.SECRET_KEY,
                       algorithm="HS256")
    return token


def request_email_confirmation(user: User, email: str) -> None:
    """Запрашивает у пользователя подтверждение почты

    """
    token = get_token(email, user.id)
    user.token_email = token
    user.is_confirmed_email = False
    user.save()
    send_mail(
        "Подтверждение почты",
        f"{settings.BASE_PROTOCOL}://{settings.BASE_DOMAIN}{settings.BASE_PORT}/auth/confirm/?token={token}",
        from_email=None,
        recipient_list=[email]
    )


def confirm_email(token: str) -> Response:
    """Подтверждает успешную верификацию почты или возвращает bad status code

    """
    try:
        decoded_token = jwt.decode(str(token), settings.SECRET_KEY, algorithms=["HS256"],
                                   options={"verify_signature": True})
        email = decoded_token["email"]
        user = User.objects.get(id=decoded_token["id"])
        if user.token_email == token:
            user.token_email = None
            user.is_confirmed_email = True
            user.email = email
            user.save()
            return Response(status=200)
        else:
            return Response(status=403)
    except jwt.ExpiredSignatureError:
        return Response({"message": "Время действия ссылки завершено, повторите попытку"}, status=408)
    except Exception as e:
        return Response(status=400)


def request_password_recovery(user: User, email: str) -> None:
    """

    """
    token = get_token(email, user.id)
    user.token_password_change = token
    user.save()
    send_mail(
        "Восстановление пароля",
        f"{settings.BASE_PROTOCOL}://{settings.BASE_DOMAIN}{settings.BASE_PORT}/auth/recovery/?token={token}",
        from_email=None,
        recipient_list=[user.email]
    )


def confirm_password_recovery(token: str, password: str) -> Response:
    try:
        decoded_token = jwt.decode(token, key=settings.SECRET_KEY, algorithms=["HS256"],
                                   options={"verify_signature": True})
    except jwt.ExpiredSignatureError:
        return Response({"message": "Закончилось время действия токена. Повторите попытку восстановления"}, status=200)
    try:
        username = decoded_token["username"]
        user = User.objects.filter(username=username)[0]
        user.token_password_change = None
        user.password = make_password(password)
        user.save()
    except Exception:
        return Response(status=400)
    return Response(status=200)
