<<<<<<< HEAD
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
=======
from fastapi import APIRouter, Depends, HTTPException
>>>>>>> 5ef8578e4793078fd9942803a0091e9ae524d78f
from auth.user_manager import hash_password, verify_password

router = APIRouter()



class SignupRequest(BaseModel):
    password: str

class VerifyRequest(BaseModel):
    password: str
    hashed_password: str

@router.post("/signup")
def signup(request: SignupRequest):
    hashed_password = hash_password(request.password)
    return {"hashed_password": hashed_password}

@router.post("/verify")
def verify(request: VerifyRequest):
    is_valid = verify_password(request.password, request.hashed_password)
    return {"valid": is_valid}



@router.post("/signup")
def signup(password: str):
    hashed_password = hash_password(password)
    return {"hashed_password": hashed_password}

@router.post("/verify")
def verify(password: str, hashed_password: str):
    is_valid = verify_password(password, hashed_password)
    return {"valid": is_valid}

