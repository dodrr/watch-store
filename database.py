from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DATABAE_URL = "postgresql://postgres:erasyl2809@localhost/watch_store"

engine = create_engine(DATABAE_URL)
SessionLocal = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass