from fastapi import APIRouter,HTTPException
from core.db import DatabaseManager
from core.email import sendemail
import random
forgotRouter = APIRouter()
@forgotRouter.get("/forgot_password")
def forgot_password(username:str=None,email:str=None):
    dm=DatabaseManager()
    dm.create_connection()
    if username:
        users=dm.fetch_query("SELECT * FROM user where name=%s LIMIT 1",(username))
    elif email:
        users=dm.fetch_query("SELECT * FROM user where email=%s LIMIT 1",(email))
    dm.close_connection()
    if len(users)==0:
        raise HTTPException(422,"该用户不存在.")
    else:
        user=users[0]
        forgotcode=''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(32))
        dm.execute_query("UPDATE user SET forgot=%s,time=now() WHERE id=%s",(forgotcode,user['id']))
        sendemail(user['email'],'邮件测试',f'验证码: {forgotcode}')
        return {"response":"已发送邮件测试."}
