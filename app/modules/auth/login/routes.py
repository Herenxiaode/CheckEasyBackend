from fastapi import APIRouter,HTTPException
from .schemas import UserLogin
from core import db
import json
import hashlib
router = APIRouter()
@router.get("/login", response_model=UserLogin)
def login(username:str,password:str):
    dm=db.DatabaseManager()
    dm.create_connection()
    users=dm.fetch_query("SELECT * FROM user where name=%s LIMIT 1",(username))
    dm.close_connection()
    if len(users)!=1:
        raise HTTPException(422,"未发现该用户.")
    else:
        user=users[0]
        md5=hashlib.md5()
        md5.update(password.encode('utf-8'))
        hex=md5.hexdigest()
        if user['verify']!=hex:
            raise HTTPException(422,"验证失败.")
        else:
            return user