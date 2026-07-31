from fastapi import FastAPI

from backend.api.routers.chat import router as chat_router
from backend.api.routers.study import router as study_router
from backend.api.routers.assignment import router as assignment_router
from backend.api.routers.placement import router as placement_router
from backend.api.routers.profile import router as profile_router

app = FastAPI(
    title="CampusPilot AI",
    version="1.0.0"
)

app.include_router(chat_router)
app.include_router(study_router)
app.include_router(assignment_router)
app.include_router(placement_router)
app.include_router(profile_router)


@app.get("/")
def home():

    return {
        "message": "CampusPilot AI Backend Running"
    }