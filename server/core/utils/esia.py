from django.conf import settings
import datetime


def get_refresh_dict(value: str = ""):
    """
    Данные для куки
    """
    return {
        "key": "refresh",
        "value": value,
        "httponly": True,
        "expires": settings.JWT_REFRESH_LIFETIME + datetime.datetime.now(),
        "samesite": "Lax"
    }
