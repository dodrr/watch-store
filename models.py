# создаем таблицу на sqlalchemy и берем инструменты как(Таблица, Строке, Числа)
from sqlalchemy import String, Integer, Column
# Из database берем наш класс Base
from database import Base
# создаем таблицу и подключаем наше название таблицы в Postgre
class Order(Base):
    __tablename__ = "orders"
# Делаем таблицу и добавляем все что нужно, часы, покупатель, цена, айди
    id = Column(Integer, primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))
    price = Column(Integer)