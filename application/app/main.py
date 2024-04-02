# Import Libries
from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from typing import List
import os

# Get Environment Variables
# DB_URL="gtuc.cxkgmu2wcs9v.us-east-1.rds.amazonaws.com"
# DATABASE_PWD="elTsgxu:zfR{k0VMi$)D|0SQxAsD"
# DATABASE_USR="postgres"
# DATABASE="gtuc"

DB_URL=os.getenv("DB_URL")
DATABASE_PWD=os.getenv("DATABASE_PWD")
DATABASE_USR=os.getenv("DATABASE_USR")
DATABASE=os.getenv("DATABASE")

DB_CREDENTIALS=f"postgresql://{DATABASE_USR}:{DATABASE_PWD}@{DB_URL}/{DATABASE}"
DATABASE_URL=DB_CREDENTIALS

# Initialize FastAPI
app = FastAPI()

@app.get("/")
async def HomePage():
    return {"message": "Welcome to AppRunner Tutorials"}

@app.get("/deploy")
async def HomePage():
    return {"message": "Testing CICD authomatic Deployment"}

# SQLAlchemy setup
SQLALCHEMY_DATABASE_URL = DATABASE_URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True, nullable=True)
    price = Column(Float)
    in_stock = Column(Boolean, default=True)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

class Item(ItemBase):
    id: int

# CRUD operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create operation
@app.post("/items/", response_model=Item)
async def create_item(item: ItemBase, db: Session = Depends(get_db)):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Read operation
@app.get("/items/", response_model=List[Item])
async def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items = db.query(ItemModel).offset(skip).limit(limit).all()
    return items

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

# Update operation
@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: ItemBase, db: Session = Depends(get_db)):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)
    db.commit()
    db.refresh(db_item)
    return db_item

# Delete operation
@app.delete("/items/{item_id}", response_model=Item)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item


# if __name__ == "__main__":
#     print("Starting webserver...")
#     uvicorn.run(
#         app,
#         host="0.0.0.0",
#         port=int(os.getenv("PORT", 8080)),
#         debug=os.getenv("DEBUG", False),
#         log_level=os.getenv('LOG_LEVEL', "info"),
#         proxy_headers=True
#     )
