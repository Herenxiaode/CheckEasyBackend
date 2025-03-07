from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class UserLogin(BaseModel):
    id: int = Field(..., description="用户编号")
    name: str = Field(..., description="用户名")
    nick: Optional[str] = Field(..., description="用户昵称")
    verify: str = Field(..., description="用户密码")
    email: str = Field(..., description="电子邮件")
