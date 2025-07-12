from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional


@dataclass
class MicroRound:
    """Representa una serie programada en un microworkout."""
    id: str
    position: int
    scheduled_time: datetime
    completed_at: Optional[datetime]


@dataclass
class MicroWorkout:
    """Entidad de dominio para un training de micropausas a lo largo del día."""
    id: str
    user_id: str
    exercise_id: str
    interval_minutes: int
    rounds: int
    created: datetime
    rounds_details: List[MicroRound]