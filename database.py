from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABASE_URL = "postgresql://postgres:erasyl2809@localhost/watch-store"

engine = DATABASE_URL
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass