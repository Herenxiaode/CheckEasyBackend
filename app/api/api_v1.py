
from fastapi import FastAPI
from modules.auth.login import routes
from modules.auth.register import registerRouter
from modules.auth.forgot_password import forgotRouter
app = FastAPI()
app.include_router(routes.router, prefix="/user")
app.include_router(registerRouter, prefix="/user")
app.include_router(forgotRouter, prefix="/user")