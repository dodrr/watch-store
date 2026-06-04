from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
orders = []
products = [
    {"brand": "Casio", "price": 56000},
    {"brand": "Rolex", "price": 67000},
    {"brand": "Hublot", "price": 15000}
]

class Order(BaseModel):
    watch: str
    customer: str

class OrderRespone(BaseModel):
    watch: str
    customer: str
    message: str

@app.get("/product")
def get_product():
    return products

@app.get("/products")
def get_products(max_price: int = None):
    if max_price:
        return [p for p in products if p["price"] <= max_price]
    return products

@app.get("/order")
def get_orders():
    return orders

@app.post("/order", response_model=OrderRespone)
def create_order(order: Order):
    orders.append(order)
    return {
        "message": "Заказ принят",
        "watch": order.watch,
        "customer": order.customer
    }

@app.put("/orders/{id}")
def update_order(order: Order, id: int):
    if id >= len(orders):
        raise HTTPException(status_code=404, detail="Заказ не найден")
    orders[id] = order
    return {
        "message": "Заказ обновлен"
    }

@app.delete("/orders/{id}")
def delete_order(id: int):
    if id >= len(orders):
        raise HTTPException(status_code=404, detail="Заказ не найден")
    orders.pop(id)
    return {
        "message": "Заказ удален"
    }