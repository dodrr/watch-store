from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
orders = []

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
    orders.append(order)
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "customer": order.customer
    }
@app.get("/orders")
def get_order():
    return orders

@app.delete("/order/{id}")
def delete_order(id: int):
    orders.pop(id)
    return {
        "message":"Заказ удален"
    }
    
@app.put("/orders/{id}")
def update_order(id: int, order: Order):
    orders[id] = order
    return {
        "message": "Заказ обновлён"
    }

