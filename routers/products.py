from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Products
from schemas import ProductSchema
from dependencies import get_db, get_current_admin

router = APIRouter() 


@router.post("/product")
def create_product(product: ProductSchema, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_product = Products(brand=product.brand, name=product.name, price=product.price)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


@router.get("/product")
def get_product(max_price: int = None, db: Session = Depends(get_db)):
    if max_price is not None:
        return db.query(Products).filter(Products.price <= max_price).all()
    return db.query(Products).all()

@router.get("/product/{id}")
def get_id_product(id: int, db:Session = Depends(get_db)):
    db_product = db.query(Products).filter(Products.id == id).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Товар не найден"
        )
    
    return db_product

@router.put("/product/{id}")
def update_product(id: int, product: ProductSchema, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_product = db.query(Products).filter(Products.id == id).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Товар не найден"
        )
    
    db_product.name = product.name
    db_product.brand = product.brand 
    db_product.price = product.price

    db.commit()
    db.refresh(db_product)
    return db_product

@router.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db), admin = Depends(get_current_admin)):

    db_product = db.query(Products).filter(Products.id == id).first()

    if not db_product:
        raise HTTPException(
            status_code=404,
            detail="Товар не найден"
        )
    
    db.delete(db_product)

    db.commit()

    return {
        "message": "Товар удален"
    }