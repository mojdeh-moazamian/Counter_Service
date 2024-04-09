from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base

SQLALCHEMY_DATABASE_URL= "sqlite:///./counters.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

