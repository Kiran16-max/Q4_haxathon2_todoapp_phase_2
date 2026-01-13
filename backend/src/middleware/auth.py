# backend/src/middleware/auth.py
from fastapi import HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlmodel import Session
from src.database import engine
from src.models.user import User
from src.utils.jwt_handler import verify_token

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = security) -> User:
    token = credentials.credentials
    email = verify_token(token)
    
    with Session(engine) as session:
        user = session.query(User).filter(User.email == email).first()
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found"
            )
        return user