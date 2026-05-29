from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    watch: str
    custamer: str

@app.get("/product")
def get_product():
    return [
        {"name": "Casio", "price": 20000},
        {"name": "Hublot", "price": 10000},
        {"name": "Rolex", "price": 15000}
    ]

@app.post("/order")
def creat_order(order: Order):
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "custamer": order.custamer
    }