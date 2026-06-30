from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Admin
from schemas import LoginSchema
from dependencies import get_db
from auth import verify_password, create_token

router = APIRouter()

@router.post("/login")
def login(admin: LoginSchema,db: Session = Depends(get_db)):
    db_admin = db.query(Admin).first()

    if not db_admin:
        raise HTTPException(
            status_code=404,
            detail="Админ не найден"
        )
    if not verify_password(admin.password, db_admin.password):
        raise HTTPException(
            status_code=401,
            detail="Неверный пароль"
        )

    token = create_token({"admin": True})

    return {
        "access_token": token,
        "token_type": "bearer"
    }

