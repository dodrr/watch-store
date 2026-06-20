from jose import jwt 
from datetime import datetime, timedelta

SECRET_KEY = "Secret"
ALGHORITM = "HS256"
TOKEN_EXPAIR_HOURS = 24

def create_token(data: dict):
    to_encode = data.copy()
    expair = datetime.utcnow() + timedelta(hours=TOKEN_EXPAIR_HOURS)
    to_encode.update({"exp": expair})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGHORITM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGHORITM])
        return payload
    except:
        return None
    
    