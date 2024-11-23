from django.apps import AppConfig


class ConsultarinvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'consultarInv'

    def ready(self):
        import consultarInv.signals
