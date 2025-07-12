import uuid
from datetime import datetime, timedelta
from typing import List, Optional

from application.ports.microworkouts import MicroWorkoutRepository
from domain.entities.microworkout import MicroWorkout, MicroRound


class MicroWorkoutService:
    """Casos de uso de la aplicación para gestionar microworkouts."""

    def __init__(self, repo: MicroWorkoutRepository) -> None:
        self._repo = repo

    def list_for_user(self, user_id: str) -> List[dict]:
        entities = self._repo.list_for_user(user_id)
        return [vars(w) for w in entities]

    def create(
        self, user_id: str, exercise_id: str, interval_minutes: int, rounds: int
    ) -> dict:
        """Genera un nuevo microworkout con rondas programadas."""
        now = datetime.utcnow()
        mw_id = str(uuid.uuid4())
        rounds_details = []
        for i in range(1, rounds + 1):
            rounds_details.append(
                MicroRound(
                    id=str(uuid.uuid4()),
                    position=i,
                    scheduled_time=now + timedelta(minutes=interval_minutes * (i - 1)),
                    completed_at=None,
                )
            )
        entity = MicroWorkout(
            id=mw_id,
            user_id=user_id,
            exercise_id=exercise_id,
            interval_minutes=interval_minutes,
            rounds=rounds,
            created=now,
            rounds_details=rounds_details,
        )
        saved = self._repo.save(entity)
        return vars(saved)

    def get_by_id(
        self, user_id: str, microworkout_id: str
    ) -> Optional[dict]:
        found = self._repo.get_by_id_for_user(user_id, microworkout_id)
        return vars(found) if found else None

    def complete_round(
        self, user_id: str, microworkout_id: str, round_id: str
    ) -> Optional[dict]:
        """Marca como completada una ronda de un microworkout."""
        entity = self._repo.get_by_id_for_user(user_id, microworkout_id)
        if not entity:
            return None
        now = datetime.utcnow()
        # actualizar la ronda correspondiente
        for r in entity.rounds_details:
            if r.id == round_id:
                r.completed_at = now
                break
        updated = self._repo.save(entity)
        return vars(updated)