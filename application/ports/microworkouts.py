from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional

from domain.entities.microworkout import MicroWorkout


class MicroWorkoutRepository(ABC):
    """Puerto de salida: contrato para persistir y recuperar microworkouts."""

    @abstractmethod
    def save(self, microworkout: MicroWorkout) -> MicroWorkout:
        """Crea o actualiza un Microworkout en la persistencia."""
        raise NotImplementedError

    @abstractmethod
    def list_for_user(self, user_id: str) -> List[MicroWorkout]:
        """Recupera todos los microworkouts de un usuario."""
        raise NotImplementedError

    @abstractmethod
    def get_by_id_for_user(
        self, user_id: str, microworkout_id: str
    ) -> Optional[MicroWorkout]:
        """Recupera un microworkout por su ID filtrado por usuario."""
        raise NotImplementedError