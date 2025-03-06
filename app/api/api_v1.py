
from fastapi import FastAPI
from modules.auth.login import routes
app = FastAPI()
app.include_router(routes.router, prefix="/user", tags=["用户"])
# app.include_router(orders_routes, prefix="/orders", tags=["订单"])
print("Initializing api_v1")