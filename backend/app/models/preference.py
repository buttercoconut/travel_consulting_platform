# preference model
from pydantic import BaseModel
from typing import List

class Preference(BaseModel):
    id: int
    user_id: int
    budget: float
    duration_days: int
    activities: List[str]
    preferred_cities: List[str]
