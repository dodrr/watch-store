# из SQLAlchemy импортируем инструменты для создание таблицы
# из database берем базовыую таблицу
from sqlalchemy import Column, Integer, String
from database import Base
# создаем таблицу и пишем имя нашей БД
class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    watch = Column(String(100))
    customer = Column(String(100))

    