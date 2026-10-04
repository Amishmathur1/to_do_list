from fastapi import APIRouter
from pydantic import BaseModel, EmailStr
from database.tables import user_detail_store
import bcrypt


class UserData(BaseModel):
    name: str
    email: EmailStr
    password: str


router = APIRouter()

@router.post('/register')
def register_user(user: UserData):
    pwd_encode = user.password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_pwd = bcrypt.hashpw(pwd_encode, salt)
    user_detail_store(user.email, hashed_pwd)
    return {
        'Message' : 'Data Added'
    }
