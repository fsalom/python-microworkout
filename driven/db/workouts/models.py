import uuid

from django.conf import settings
from django.db import models


class Workout(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='workouts'
    )
    date = models.DateField()
    name = models.CharField(max_length=100)
    notes = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


class Exercise(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)


class WorkoutExercise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout = models.ForeignKey(
        Workout, related_name='exercises', on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        Exercise, on_delete=models.PROTECT
    )
    order = models.PositiveSmallIntegerField()


class WorkoutSet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout_exercise = models.ForeignKey(
        WorkoutExercise, related_name='sets', on_delete=models.CASCADE
    )
    reps = models.PositiveSmallIntegerField()
    weight_kg = models.FloatField(null=True, blank=True)
    rest_sec = models.PositiveSmallIntegerField(default=0)