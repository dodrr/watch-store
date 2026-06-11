from sqlalchemy import String, Integer, Column
from database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))
    price = Column(Integer)

