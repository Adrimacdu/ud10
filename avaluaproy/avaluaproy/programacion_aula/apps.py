from django.apps import AppConfig


class ProgramacionAulaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # UD6.4.d
    name = 'programacion_aula'
    verbose_name = 'programacion_aula'

#UD9.5 
class ProgramacionAulaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'programacion_aula'

    def ready(self):
        import programacion_aula.signals