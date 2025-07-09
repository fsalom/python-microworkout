from __future__ import annotations
from dataclasses import dataclass
from datetime import date
from typing import List, Optional


@dataclass
class WorkoutSet:
    """Serie realizada dentro de un ejercicio de gimnasio."""
    reps: int
    weight_kg: Optional[float]
    rest_sec: int


@dataclass
class WorkoutExercise:
    """Ejercicio dentro del workout, con sus series."""
    exercise_id: str
    order: int
    sets: List[WorkoutSet]


@dataclass
class Workout:
    """Entidad de dominio que representa un entrenamiento completo."""
    id: str
    user_id: str
    date: date
    name: str
    notes: Optional[str]
    exercises: List[WorkoutExercise]
    created: date
    modified: date