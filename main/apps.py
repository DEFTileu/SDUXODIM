from django.apps import AppConfig


from django.apps import AppConfig

from django.apps import AppConfig

class TicketsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    def ready(self):
        app_label = 'main'
        from main.sender import start_reminder_loop
        start_reminder_loop()
