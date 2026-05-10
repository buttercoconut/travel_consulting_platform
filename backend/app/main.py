from fastapi import FastAPI
from .api import travel_plan

app = FastAPI(title="Travel Consulting Platform API")

app.include_router(travel_plan.router)
