import datetime
import os

import bcrypt
import jwt
from database.tables import login_pass_retrival, user_detail_store
from dotenv import load_dotenv  # pyright: ignore[reportMissingImports]
from fastapi import (  # pyright: ignore[reportMissingImports]
    APIRouter,
    HTTPException,
    status,
)
from pydantic import BaseModel, EmailStr  # pyright: ignore[reportMissingImports]

load_dotenv()
SECRET_KEY = os.getenv('jwt_key')

class UserData(BaseModel):
    name: str
    email: EmailStr
    password: str

class loginData(BaseModel):
    email: EmailStr
    password: str


router = APIRouter()

@router.post('/register')
def register_user(user: UserData):
    pwd_encode = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_encode, salt)
    hashed_pwd = hashed_pwd.decode('utf-8')

    user_detail_store(user.email, hashed_pwd)
    return {
        'Message' : 'Data Added'
    }

@router.post('/login')
def login_user(userDetails: loginData):
    mail = userDetails.email
    fetched = login_pass_retrival(mail)

    if fetched is None:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Email or Password dosn't match"
        )

    pwd = userDetails.password.encode('utf-8')
    userId = fetched[0]

    if bcrypt.checkpw(pwd, fetched[1].encode('utf-8')):
        payload = {
            "sub": str(userId),
            "iat": datetime.datetime.now(datetime.timezone.utc),
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=5)
        }

        token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")  # pyright: ignore[reportArgumentType]
        return {
            'Encoded Token' : token
        }

    else:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail = "Email or Password dosn't match"
        )