import uuid
from typing import List, Optional

from application.ports.workouts import WorkoutRepository
from domain.entities.workout import (
    Workout as DomainWorkout,
    WorkoutExercise as DomainWorkoutExercise,
    WorkoutSet as DomainWorkoutSet,
)


class WorkoutService:
    """Caso de uso de la aplicación para gestionar workouts."""

    def __init__(self, repo: WorkoutRepository) -> None:
        self._repo = repo

    def list_for_user(self, user_id: str) -> List[dict]:
        """Obtiene todos los workouts de un usuario."""
        domain_list = self._repo.list_for_user(user_id)
        return [vars(w) for w in domain_list]

    def create(self, user_id: str, dto) -> dict:
        """Crea un nuevo workout a partir de un DTO de entrada."""
        workout_id = str(uuid.uuid4())
        entity = DomainWorkout(
            id=workout_id,
            user_id=user_id,
            date=dto.date,
            name=dto.name,
            notes=dto.notes,
            exercises=[
                DomainWorkoutExercise(
                    exercise_id=e.exercise_id,
                    order=e.order,
                    sets=[
                        DomainWorkoutSet(
                            reps=s.reps,
                            weight_kg=s.weight_kg,
                            rest_sec=s.rest_sec,
                        )
                        for s in e.sets
                    ],
                )
                for e in dto.exercises
            ],
            created=None,
            modified=None,
        )
        saved = self._repo.save(entity)
        return vars(saved)

    def get_by_id(self, user_id: str, workout_id: str) -> Optional[dict]:
        """Recupera un workout concreto por ID y usuario."""
        found = self._repo.get_by_id_for_user(user_id, workout_id)
        return vars(found) if found else None