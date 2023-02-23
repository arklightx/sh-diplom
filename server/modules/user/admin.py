from django.contrib import admin
from .models import User, AccessTokens, RefreshTokens

admin.site.register(User)


@admin.register(AccessTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to")


@admin.register(RefreshTokens)
class AccessTokens(admin.ModelAdmin):
    list_display = ("token", "user", "valid_to", "access")
