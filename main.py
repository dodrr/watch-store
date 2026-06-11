from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Order, Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

class OrderSchema(BaseModel):
    watch: str
    customer: str
    price: int

@app.post("/order")
def create_order(order: OrderSchema, db: Session = Depends(get_db)):
    db_order = Order(watch=order.watch, customer=order.customer, price=order.price)

    db.add(db_order)

    db.commit()

    db.refresh(db_order)

    return db_order

@app.get("/orders")
def get_order(db: Session = Depends(get_db), max_price: int = None):
    if max_price:
        return db.query(Order).filter(Order.price <= max_price).all()
    return db.query(Order).all()

@app.put("/orders/{id}")
def update_order(id: int,order: OrderSchema, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    db_order.watch = order.watch
    db_order.customer = order.customer

    db.commit()

    db.refresh(db_order)

    return db_order

@app.delete("/orders/{id}")
def delete_order(id: int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    db.delete(db_order)

    db.commit()

    return {
        "message": "Заказ удален"
    }

