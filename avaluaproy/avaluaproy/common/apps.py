from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # UD6.4.d
    name = 'common'
    verbose_name = 'common'
