from fastapi import APIRouter,HTTPException
from core import db
import hashlib
registerRouter = APIRouter()
@registerRouter.get("/register")
def register(username:str,password:str,email:str):
    dm=db.DatabaseManager()
    dm.create_connection()
    users=dm.fetch_query("SELECT * FROM user where name=%s LIMIT 1",(username))
    dm.close_connection()
    if len(users)!=0:
        raise HTTPException(422,"该用户已存在.")
    else:
        md5=hashlib.md5()
        md5.update(password.encode('utf-8'))
        verify=md5.hexdigest()
        dm.execute_query("INSERT INTO user(name,verify,email)VALUES(%s,%s,%s)",(username,verify,email))
        # 备注:需要判断是否添加成功?
        return {"response":"注册完毕."}