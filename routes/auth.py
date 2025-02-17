from fastapi import APIRouter, Depends, HTTPException
from auth.user_manager import hash_password, verify_password

router = APIRouter()

@router.post("/signup")
def signup(password: str):
    hashed_password = hash_password(password)
    return {"hashed_password": hashed_password}

@router.post("/verify")
def verify(password: str, hashed_password: str):
    is_valid = verify_password(password, hashed_password)
    return {"valid": is_valid}
