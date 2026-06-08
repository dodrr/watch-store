from fastapi import FastAPI, HTTPException,Depends
from pydantic import BaseModel
from database import SessionLocal, engine
from models import Base, Order
from sqlalchemy.orm import Session

app = FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class OrderSchem(BaseModel):
    watch: str
    customer: str

@app.post("/order")
def create_order(order: OrderSchem, db: Session = Depends(get_db)):
    db_order = Order(watch=order.watch, customer=order.customer)

    db.add(db_order)

    db.commit()
    
    db.refresh(db_order)

    return db_order

@app.get("/orders")
def get_order(db: Session = Depends(get_db)):
    db.query(Order).all


@app.put("orders/{id}")
def update(id: int, order: OrderSchem, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).filter()

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")

    db_order.watch = order.watch
    db_order.customer = order.customer

    db.commit()
    db.refresh(db_order)
    
    return db_order

@app.delete("/orders/{id}")
def delete_order()