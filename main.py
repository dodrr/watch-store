from fastapi import FastAPI,HTTPException, Depends
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal
from models import Order, Products, Base
from auth import verify_token, create_token

app = FastAPI()
Base.metadata.create_all(bind=engine)
security = HTTPBearer()

def get_current_admin(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials 
    payload = verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Неверный токен")
    return payload

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

class ProductSchema(BaseModel):
    name: str
    brand: str
    price: int 

class Admin_Login(BaseModel):
    password: str

ADMIN_PASSWORD = "123"

@app.post("/admin/login")
def get_admin_login(data: Admin_Login):
    if data.password != ADMIN_PASSWORD:
        raise HTTPException(status_code=401, detail="Неверный пароль")
    token = create_token({"sub": "admin"})
    return {"token": token}

@app.post("/product")
def create_product(product: ProductSchema, admin = Depends(get_current_admin),db: Session = Depends(get_db)):
    db_product = Products(name=product.name, brand=product.brand, price=product.price)

    db.add(db_product)

    db.commit()
    
    db.refresh(db_product)
    
    return db_product 


@app.get("/products")
def get_products(db: Session = Depends(get_db), max_price: int = None):
    if max_price:
        return db.query(Products).filter(Products.price <= max_price).all()
    return db.query(Products).all()

@app.get("/products/{id}")
def get_product_id(id: int, db: Session = Depends(get_db)):    
    db_product = db.query(Products).filter(Products.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="продукт не найден")    
    return db_product

@app.put("/products/{id}")
def update_product(id:int, product: ProductSchema, admin = Depends(get_current_admin), db: Session = Depends(get_db)):
    db_product = db.query(Products).filter(Products.id == id).first()

    if not db_product:
        raise HTTPException(status_code=404, detail="продукт не найден")
    
    db_product.brand = product.brand
    db_product.name = product.name 
    db_product.price = product.price

    db.commit()

    db.refresh(db_product)

    return db_product

@app.delete("/products/{id}")
def delete_product(id:int, admin = Depends(get_current_admin), db: Session = Depends(get_db)):
    db_product = db.query(Products).filter(Products.id == id).first() 

    if not db_product:
        raise HTTPException(status_code=404, detail="продукт не найден")

    db.delete(db_product) 

    db.commit()

    return db_product 


@app.post("/orders")
def create_orders(order: OrderSchema, db: Session = Depends(get_db),):
    db_order = Order(watch=order.watch, customer=order.customer, price=order.price)

    db.add(db_order)

    db.commit()

    db.refresh(db_order)

    return db_order 

@app.get("/orders")
def get_orders(db: Session = Depends(get_db)):
    db_order = db.query(Order).all()

    return db_order 

@app.get("/orders/{id}")
def get_order_id(id:int, db: Session = Depends(get_db)):
    db_order = db.query(Order).filter(Order.id == id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    return db_order

@app.put("/orders/{id}")
def update_order(id: int,order: OrderSchema, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_order = db.query(Order).filter(Order.id == id).first()

    if not db_order:
        raise HTTPException(status_code=404, detail="Заказ не найден")
    
    db_order.watch = order.watch
    db_order.customer = order.customer
    db_order.price = order.price 

    db.commit()

    db.refresh(db_order)

    return db_order

@app.delete("/orders/{id}")
def delete_order(id: int,db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    db_order = db.query(Order).filter(Order.id == id).first() 

    if not db_order:
         raise HTTPException(status_code=404, detail="Заказ не найден") 
    
    db.delete(db_order)

    db.commit()

    return {
        "message": "Заказ удален"
    }