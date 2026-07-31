from fastapi import FastAPI

from app.database import engine
from app import models
import app.routers.auth as auth
import app.routers.profile as profile
import app.routers.resume as resume

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerPilot AI",
    description="Backend API for CareerPilot AI",
    version="1.0.0"
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    profile.router,
    prefix="/profile",
    tags=["Profile"]
)
app.include_router(
    resume.router,
    prefix="/resume",
    tags=["Resume"]
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPilot AI Backend 🚀"
    }
