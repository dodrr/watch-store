from sqlalchemy import String, Column, Integer
from database import Base

class Products(Base):
    __tablename__ = "products"
    id = Column(Integer,primary_key=True)
    name = Column(String(100))
    brand = Column(String(100))
    price = Column(Integer)
    category = Column(String(100))

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer,primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))
    price = Column(Integer)

    