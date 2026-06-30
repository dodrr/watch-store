from fastapi import FastAPI
from database import Base, engine
from routers.products import router as product_router
from routers.orders import router as order_router
from routers.admin import router as admin_router

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(product_router)
app.include_router(order_router)
app.include_router(admin_router)

