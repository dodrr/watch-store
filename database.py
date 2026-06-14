# из sqlalchemy берем инструменты которые озночают - создание БД, и подключение
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
# подключаем свой postgresql
DATABASE_URL = "postgresql://postgres:erasyl2809@localhost/watch_store"# подуючение склб(а точнее с скюлалхкеми на постреге)
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass