## Import Libries
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base
import os

#Get Environment Variables
DB_URL=os.getenv("DB_URL")
DATABASE=os.getenv("DATABASE")
DATABASE_PWD=os.getenv("DATABASE_PWD")
DATABASE_USR=os.getenv("DATABASE_USR")

# Setup Database Credentials
DATABASE_URL=f"postgresql://{DATABASE_USR}:{DATABASE_PWD}@{DB_URL}/{DATABASE}"

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Database model
Base = declarative_base()

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)