from typing import List, Optional
from uuid import UUID

from django.db import transaction

from application.ports.workouts import WorkoutRepository
from domain.entities.workout import (
    Workout as DomainWorkout,
    WorkoutExercise as DomainWorkoutExercise,
    WorkoutSet as DomainWorkoutSet,
)
from .models import Workout, WorkoutExercise, WorkoutSet, Exercise


class DjangoORMWorkoutRepository(WorkoutRepository):
    """Implementación de WorkoutRepository usando Django ORM."""

    def save(self, workout: DomainWorkout) -> DomainWorkout:
        with transaction.atomic():
            obj, _ = Workout.objects.update_or_create(
                id=UUID(workout.id),
                defaults={
                    'user_id': workout.user_id,
                    'date': workout.date,
                    'name': workout.name,
                    'notes': workout.notes,
                },
            )
            obj.exercises.all().delete()
            for exc in workout.exercises:
                exercise_obj, _ = Exercise.objects.get_or_create(
                    id=exc.exercise_id,
                    defaults={'name': exc.exercise_id},
                )
                we_obj = WorkoutExercise.objects.create(
                    workout=obj,
                    exercise=exercise_obj,
                    order=exc.order,
                )
                for s in exc.sets:
                    WorkoutSet.objects.create(
                        workout_exercise=we_obj,
                        reps=s.reps,
                        weight_kg=s.weight_kg,
                        rest_sec=s.rest_sec,
                    )
            return self._to_domain(obj)

    def list_for_user(self, user_id: str) -> List[DomainWorkout]:
        qs = Workout.objects.filter(user_id=user_id).order_by('-date', '-created')
        return [self._to_domain(o) for o in qs]

    def get_by_id_for_user(
        self, user_id: str, workout_id: str
    ) -> Optional[DomainWorkout]:
        try:
            obj = Workout.objects.get(id=UUID(workout_id), user_id=user_id)
        except Workout.DoesNotExist:
            return None
        return self._to_domain(obj)

    def _to_domain(self, obj: Workout) -> DomainWorkout:
        exercises = []
        for we in obj.exercises.order_by('order').all():
            sets = [
                DomainWorkoutSet(
                    reps=s.reps,
                    weight_kg=s.weight_kg,
                    rest_sec=s.rest_sec,
                )
                for s in we.sets.all()
            ]
            exercises.append(
                DomainWorkoutExercise(
                    exercise_id=we.exercise.id,
                    order=we.order,
                    sets=sets,
                )
            )
        return DomainWorkout(
            id=str(obj.id),
            user_id=str(obj.user_id),
            date=obj.date,
            name=obj.name,
            notes=obj.notes,
            exercises=exercises,
            created=obj.created,
            modified=obj.modified,
        )