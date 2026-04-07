from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserRegister
from app.models.user import User 
from app.db.database import get_db
from app.core.security import hash_password
from app.schemas.user import UserRegister

router = APIRouter(prefix="/auth", tags =["auth"])

@router.post("/register")
def register(user: UserRegister, db: Session = Depends(get_db)):
    
    #check if user exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Hash Password
    hashed_password = hash_password(user.password)

    #create user
    new_user = User(
        full_name=user.full_name,
        email=user.email,
        password_hash=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"Message: User created Successfully"}