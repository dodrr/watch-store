from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Order(BaseModel):
    watch: str
    customer: str

@app.get("/product")
def get_product():
    return [
        {"name": "Casio", "price": 19000},
        {"name": "Hublot", "price": 20000},
        {"name": "Patek Philippe", "price": 21234}
    ]

@app.post("/order")
def creat_oreder(order: Order):
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "customer": order.customer
    }