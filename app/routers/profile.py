print("✅ profile.py loaded")
from fastapi import APIRouter, Depends

from app.models import User
from app.security import get_current_user

router = APIRouter()


@router.get("/me")
def get_profile(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email
    }