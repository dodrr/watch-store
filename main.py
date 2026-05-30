from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    watch: str
    customer: str

@app.get("/product")
def get_products():
    return [
        {"name": "Casio", "price": 13400},
        {"name": "Hublot", "price": 45000},
        {"name": "Rolex", "price": 44234}
    ]

@app.post("/order")
def creat_order(order: Order):
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "customer": order.customer
    }