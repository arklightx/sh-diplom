from django.apps import AppConfig


class VotesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.votes'
    verbose_name = "Голосования"
