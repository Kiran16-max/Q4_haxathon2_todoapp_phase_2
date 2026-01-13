# backend/src/services/auth_service.py
import bcrypt
from sqlmodel import Session
from passlib.context import CryptContext
from src.models.user import User, UserCreate

# Password hashing context with proper bcrypt configuration
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__ident="2b",
    bcrypt__rounds=12,
)

def hash_password_with_limit(password: str) -> str:
    """
    Hash a password ensuring it doesn't exceed bcrypt's 72-byte limit.
    Truncates the password if necessary before hashing.
    """
    # Convert to bytes and limit to 72 bytes for bcrypt
    password_bytes = password.encode('utf-8')
    if len(password_bytes) > 72:
        # Truncate to 72 bytes to comply with bcrypt limits
        password_bytes = password_bytes[:72]
        # Decode back to string for hashing
        password = password_bytes.decode('utf-8', errors='ignore')

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_user(user: UserCreate, session: Session) -> User:
    # Hash the password
    hashed_password = get_password_hash(user.password)

    # Create the user object
    db_user = User(
        email=user.email,
        name=user.name,
        password_hash=hashed_password
    )

    # Add to session and commit
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user

def authenticate_user(email: str, password: str, session: Session) -> User:
    # Find user by email
    user = session.query(User).filter(User.email == email).first()

    # Verify user exists and password is correct
    if not user or not verify_password(password, user.password_hash):
        return None

    return user