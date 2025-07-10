from abc import ABC, abstractmethod
from typing import List, Optional

from domain.entities.workout import Workout as DomainWorkout


class WorkoutRepository(ABC):
    """Puerto de salida: contrato para persistir y recuperar workouts."""

    @abstractmethod
    def save(self, workout: DomainWorkout) -> DomainWorkout:
        """Crea o actualiza un Workout en la persistencia."""
        raise NotImplementedError

    @abstractmethod
    def list_for_user(self, user_id: str) -> List[DomainWorkout]:
        """Recupera todos los workouts de un usuario."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id_for_user(
        self, user_id: str, workout_id: str
    ) -> Optional[DomainWorkout]:
        """Recupera un workout por su ID, filtrando por usuario."""
        raise NotImplementedError