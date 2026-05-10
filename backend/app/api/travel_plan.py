from fastapi import APIRouter, Depends
from datetime import datetime
from typing import List
from ..models.user import User
from ..models.preference import Preference
from ..models.travel_plan import TravelPlan
from ..services.travel_plan_service import TravelPlanService

router = APIRouter(prefix="/travel-plans", tags=["travel-plans"])

# Dummy dependency for user
async def get_current_user() -> User:
    return User(id=1, email="john@example.com", name="John", created_at=datetime.utcnow())

@router.post("/", response_model=TravelPlan)
async def create_travel_plan(preference: Preference, user: User = Depends(get_current_user)):
    service = TravelPlanService()
    plan = service.generate_plan(user, preference)
    return plan
