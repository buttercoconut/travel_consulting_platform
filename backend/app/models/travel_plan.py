# travel_plan model
from pydantic import BaseModel
from datetime import datetime
from typing import List

class TravelPlan(BaseModel):
    id: int
    user_id: int
    title: str
    description: str
    start_date: datetime
    end_date: datetime
    created_at: datetime
    itinerary: List[dict] = []
