from django.apps import AppConfig

class RegistrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'registration'

    def ready(self):
        from registration import signals  # Import signal handlers
