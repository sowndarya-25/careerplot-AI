from fastapi import FastAPI
from app.database import engine
from app import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CareerPilot AI",
    description="Backend API for CareerPilot AI",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to CareerPilot AI Backend 🚀"
    }