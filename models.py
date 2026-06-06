from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))

    