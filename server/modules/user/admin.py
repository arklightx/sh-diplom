from django.contrib import admin
from .models import AccessTokens, RefreshTokens


@admin.register(AccessTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to")


@admin.register(RefreshTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to", "access")
