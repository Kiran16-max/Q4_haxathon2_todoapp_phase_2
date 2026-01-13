# # backend/src/api/auth.py
# from fastapi import APIRouter, Depends
# from sqlmodel import Session
# from src.database import engine
# from src.models.user import User, UserCreate, UserRead
# from src.services.auth_service import create_user, authenticate_user
# from src.utils.jwt_handler import create_access_token
# from src.utils.api_responses import success_response, error_response

# router = APIRouter()

# def get_session():
#     with Session(engine) as session:
#         yield session

# @router.post("/auth/register", response_model=UserRead)
# def register(user: UserCreate, session: Session = Depends(get_session)):
#     # Check if user already exists
#     existing_user = session.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         from fastapi import HTTPException
#         raise HTTPException(status_code=409, detail="Email already registered")

#     # Create new user
#     db_user = create_user(user=user, session=session)
#     return db_user

# @router.post("/auth/login")
# def login(email: str, password: str, session: Session = Depends(get_session)):
#     user = authenticate_user(email=email, password=password, session=session)
#     if not user:
#         from fastapi import HTTPException
#         raise HTTPException(status_code=401, detail="Incorrect email or password")

#     # Create access token
#     access_token = create_access_token(data={"sub": user.email})

#     return {
#         "access_token": access_token,
#         "token_type": "bearer",
#         "user": {
#             "id": user.id,
#             "email": user.email,
#             "name": user.name
#         }
#     }









# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from sqlmodel import Session
# from src.database import engine
# from src.models.user import User, UserCreate, UserRead
# from src.services.auth_service import create_user, authenticate_user
# from src.utils.jwt_handler import create_access_token

# router = APIRouter()

# def get_session():
#     with Session(engine) as session:
#         yield session

# @router.post("/auth/register")
# def register(user: UserCreate, session: Session = Depends(get_session)):
#     existing_user = session.query(User).filter(User.email == user.email).first()
#     if existing_user:
#         raise HTTPException(status_code=409, detail="Email already registered")

#     db_user = create_user(user=user, session=session)

#     token = create_access_token({"sub": db_user.email})

#     return {
#         "access_token": token,
#         "token_type": "bearer",
#         "user": {
#             "id": db_user.id,
#             "email": db_user.email,
#             "name": db_user.name
#         }
#     }

# @router.post("/auth/login")
# def login(
#     form_data: OAuth2PasswordRequestForm = Depends(),
#     session: Session = Depends(get_session)
# ):
#     user = authenticate_user(
#         email=form_data.username,
#         password=form_data.password,
#         session=session
#     )

#     if not user:
#         raise HTTPException(status_code=401, detail="Incorrect email or password")

#     token = create_access_token({"sub": user.email})

#     return {
#         "access_token": token,
#         "token_type": "bearer",
#         "user": {
#             "id": user.id,
#             "email": user.email,
#             "name": user.name
#         }
#     }







from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session
from src.database import engine
from src.models.user import User, UserCreate, UserRead
from src.services.auth_service import create_user, authenticate_user
from src.utils.jwt_handler import create_access_token
from src.utils.logger import logger  # optional but recommended

router = APIRouter()

# Dependency to get DB session
def get_session():
    with Session(engine) as session:
        yield session

# ---------------------------
# REGISTER ENDPOINT
# ---------------------------
@router.post("/auth/register")
def register(user: UserCreate, session: Session = Depends(get_session)):
    logger.info(f"Register request for email: {user.email}")

    # Check if user already exists
    existing_user = session.query(User).filter(User.email == user.email).first()
    if existing_user:
        logger.warning(f"Email already registered: {user.email}")
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    # Create new user
    db_user = create_user(user=user, session=session)
    token = create_access_token(data={"sub": db_user.email})
    logger.info(f"User registered successfully: {db_user.id}")

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": db_user.id,
            "email": db_user.email,
            "name": db_user.name
        }
    }

# ---------------------------
# LOGIN ENDPOINT
# ---------------------------
@router.post("/auth/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session)
):
    logger.info(f"Login attempt for email: {form_data.username}")

    user = authenticate_user(
        email=form_data.username,
        password=form_data.password,
        session=session
    )

    if not user:
        logger.warning(f"Failed login attempt: {form_data.username}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(data={"sub": user.email})
    logger.info(f"User logged in successfully: {user.id}")

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": user.id,
            "email": user.email,
            "name": user.name
        }
    }
