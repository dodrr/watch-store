from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI() 
orders = []
products = [
    {"brand": "Casio", "price": 10000},
    {"brand": "Hyblot", "price": 145444},
    {"brand": "Patek philippe", "price": 45555}
]

class Order(BaseModel):
    watch: str
    customer: str

@app.get("/product")
def get_product():
    return products

@app.get("/products")
def search_order(max_price: int = None):

    if max_price:
        return [p for p in products if p["price"] <= max_price]
    else:
        return products

@app.post("/order")
def creat_order(order: Order):
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
    if id >= len(orders):
        raise HTTPException(status_code=404, detail="Заказ не")
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


