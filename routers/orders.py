from fastapi import APIRouter, Depends, HTTPException 
from sqlalchemy.orm import Session
from models import Orders
from dependencies import get_db, get_current_admin
from schemas import OrderSchema

router = APIRouter()

@router.post("/order")
def create_order(order: OrderSchema, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_order = Orders(watch=order.watch, customer=order.customer, price=order.price)

    db.add(db_order)
    db.commit()
    db.refresh(db_order)

    return db_order

@router.get("/order")
def get_order(db: Session = Depends(get_db)):
    return db.query(Orders).all()


@router.get("/order/{id}")
def get_id_order(id: int, db: Session = Depends(get_db)):
    db_order = db.query(Orders).filter(Orders.id == id).first()

    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Заказ не найден"
        )
    
    return db_order

@router.put("/order/{id}")
def update_order(id: int, order: OrderSchema, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_order = db.query(Orders).filter(Orders.id == id).first()

    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Заказ не найден"

        )
    
    db_order.watch = order.watch
    db_order.customer = order.customer
    db_order.price = order.price

    db.commit()
    db.refresh(db_order)

    return db_order

@router.delete("/order/{id}")
def delete_order(id: int, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_order = db.query(Orders).filter(Orders.id == id).first()

    if not db_order:
        raise HTTPException(
            status_code=404,
            detail="Заказ не найден"

        )
    db.delete(db_order)
    db.commit()

    return {
        "message": "Заказ удален"
    }