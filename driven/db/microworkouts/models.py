import uuid

from django.conf import settings
from django.db import models


class MicroWorkout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='microworkouts'
    )
    exercise_id = models.CharField(max_length=50)
    interval_minutes = models.PositiveSmallIntegerField()
    total_rounds = models.PositiveSmallIntegerField()
    created = models.DateTimeField(auto_now_add=True)


class MicroRound(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    microworkout = models.ForeignKey(
        MicroWorkout, related_name='rounds', on_delete=models.CASCADE
    )
    position = models.PositiveSmallIntegerField()
    scheduled_time = models.DateTimeField()
    completed_at = models.DateTimeField(blank=True, null=True)