# Service for travel plan generation
from typing import List
from datetime import datetime
from ..models.user import User
from ..models.preference import Preference
from ..models.travel_plan import TravelPlan

class TravelPlanService:
    def __init__(self):
        # In real scenario, inject DB session or external APIs
        pass

    def generate_plan(self, user: User, preference: Preference) -> TravelPlan:
        # Simplified logic: create a plan with dummy itinerary
        plan = TravelPlan(
            id=1,
            user_id=user.id,
            title=f"{user.name}'s {preference.duration_days}-day trip",
            description="Generated based on your preferences.",
            start_date=datetime.utcnow(),
            end_date=datetime.utcnow(),
            created_at=datetime.utcnow(),
            itinerary=[
                {"day": 1, "city": city, "activity": act}
                for city, act in zip(preference.preferred_cities, preference.activities)
            ],
        )
        return plan
