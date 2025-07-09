from datetime import date
from typing import List, Optional

from pydantic import BaseModel, Field


class WorkoutSetIn(BaseModel):
    reps: int
    weight_kg: Optional[float] = None
    rest_sec: int = 0


class WorkoutExerciseIn(BaseModel):
    exercise_id: str
    order: int
    sets: List[WorkoutSetIn]


class WorkoutIn(BaseModel):
    date: date
    name: str = Field(..., max_length=100)
    notes: Optional[str]
    exercises: List[WorkoutExerciseIn]


class WorkoutSetOut(WorkoutSetIn):
    id: str


class WorkoutExerciseOut(WorkoutExerciseIn):
    id: str
    sets: List[WorkoutSetOut]


class WorkoutOut(BaseModel):
    id: str
    user_id: str
    date: date
    name: str
    notes: Optional[str]
    exercises: List[WorkoutExerciseOut]
    created: date
    modified: date