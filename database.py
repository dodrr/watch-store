# импортируем с склю подкючение БД и сесси 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# пишем свой парооль и подключаем к нашему бд
DATABASE_URL = "postgresql://postgres:erasyl2809@localhost/watch_store"
# подключаем бд
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

# базовый класс для всех таблиц
class Base(DeclarativeBase):
    pass