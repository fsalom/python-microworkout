from typing import List, Optional
from uuid import UUID

from django.db import transaction

from application.ports.microworkouts import MicroWorkoutRepository
from domain.entities.microworkout import MicroWorkout as DomainMW, MicroRound as DomainRound
from .models import MicroWorkout, MicroRound


class DjangoORMMicroWorkoutRepository(MicroWorkoutRepository):
    """Implementación de MicroWorkoutRepository usando Django ORM."""

    def save(self, microworkout: DomainMW) -> DomainMW:
        with transaction.atomic():
            mw_obj, _ = MicroWorkout.objects.update_or_create(
                id=UUID(microworkout.id),
                defaults={
                    'user_id': microworkout.user_id,
                    'exercise_id': microworkout.exercise_id,
                    'interval_minutes': microworkout.interval_minutes,
                    'total_rounds': microworkout.rounds,
                    'created': microworkout.created,
                },
            )
            mw_obj.rounds.all().delete()
            for r in microworkout.rounds_details:
                MicroRound.objects.create(
                    id=UUID(r.id),
                    microworkout=mw_obj,
                    position=r.position,
                    scheduled_time=r.scheduled_time,
                    completed_at=r.completed_at,
                )
            return self._to_domain(mw_obj)

    def list_for_user(self, user_id: str) -> List[DomainMW]:
        qs = MicroWorkout.objects.filter(user_id=user_id).order_by('-created')
        return [self._to_domain(mw) for mw in qs]

    def get_by_id_for_user(
        self, user_id: str, microworkout_id: str
    ) -> Optional[DomainMW]:
        try:
            mw_obj = MicroWorkout.objects.get(id=UUID(microworkout_id), user_id=user_id)
        except MicroWorkout.DoesNotExist:
            return None
        return self._to_domain(mw_obj)

    def _to_domain(self, mw_obj: MicroWorkout) -> DomainMW:
        rounds = []
        for r in mw_obj.rounds.order_by('position'):
            rounds.append(
                DomainRound(
                    id=str(r.id),
                    position=r.position,
                    scheduled_time=r.scheduled_time,
                    completed_at=r.completed_at,
                )
            )
        return DomainMW(
            id=str(mw_obj.id),
            user_id=str(mw_obj.user_id),
            exercise_id=mw_obj.exercise_id,
            interval_minutes=mw_obj.interval_minutes,
            rounds=mw_obj.total_rounds,
            created=mw_obj.created,
            rounds_details=rounds,
        )