from jose import jwt, JWTError
from datetime import datetime,timedelta
from passlib.context import CryptContext

SECRET_KEY = "secret"
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24

pwd_context = CryptContext(schemes=["bcrypt"]) 

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(password:str, hashed_password):
    return pwd_context.verify(password,hashed_password)

def create_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow + timedelta(hours=TOKEN_EXPIRE_HOURS)
    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
    
    
