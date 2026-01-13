# backend/src/utils/jwt_handler.py
from datetime import datetime, timedelta
from typing import Optional
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from sqlmodel import Session
from src.database import engine
from src.models.user import User

import os
from pydantic_settings import BaseSettings
from src.utils.logger import logger  # Import logger at the top

# Configuration class for JWT settings
class Settings(BaseSettings):
    secret_key: str = os.getenv("BETTER_AUTH_SECRET", "fallback-test-key-change-in-production")  # Use environment variable
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

settings = Settings()

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

security = HTTPBearer()

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        logger.info(f"Attempting to decode JWT token: {token[:20]}...")  # Log first 20 chars of token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        logger.info(f"Successfully decoded JWT, email: {email}")
        if email is None:
            raise credentials_exception
    except JWTError as e:
        logger.error(f"JWT decoding failed: {str(e)}")
        raise credentials_exception
    return email

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
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