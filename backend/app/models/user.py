from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class User(BaseModel):
    id: int
    email: str
    name: str
    created_at: datetime

class Preference(BaseModel):
    id: int
    user_id: int
    budget: float
    duration_days: int
    activities: List[str]
    preferred_cities: List[str]

class TravelPlan(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str] = None
    start_date: datetime
    end_date: datetime
    created_at: datetime
    preferences: Preference
    recommended_products: List[int] = []
