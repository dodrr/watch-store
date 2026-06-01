from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
orders = []
products = [
        {"name": "Casio", "price": 59000},
        {"name": "Patek Philippe", "price": 40000},
        {"name": "Hyblot", "price": 10000}
    ]

class Order(BaseModel):
    watch: str
    customer: str

@app.get("/products")
def get_products(max_price: int = None):
    if max_price:
        return  [p for p in products if p["price"] <= max_price]
    else:
        return products


@app.post("/order")
def chech_order(order: Order):
    orders.append(order)
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "customer": order.customer
    }
@app.get("/orders")
def get_orders():
    return orders

@app.put("/orders/{id}")
def update_order(id: int, order: Order):
    orders[id] = order
    return {
        "message": "Заказ обновлен",

    }

@app.delete("/order/{id}")
def delete_order(id: int):
    orders.pop(id)
    return {
        "message": "Заказ удален"
    }

