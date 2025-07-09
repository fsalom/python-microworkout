from django.apps import AppConfig


class WorkoutsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'driven.db.workouts'
    label = 'workouts'

    def ready(self):
        # Importar modelos para que Django los detecte
        from .models import Workout  # noqa
        from .models import WorkoutExercise, WorkoutSet, Exercise  # noqa