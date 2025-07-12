from django.apps import AppConfig


class MicroWorkoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'driven.db.microworkouts'
    label = 'microworkouts'

    def ready(self):
        from .models import MicroWorkout, MicroRound  # noqa