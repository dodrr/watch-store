from sqlalchemy import String, Integer, Column
from database import Base

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    brand = Column(String(100))
    cotegory = Column(String(100))
    price = Column(Integer)

class Orders(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))
    price = (Integer)

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True)
    password = Column(String(255))