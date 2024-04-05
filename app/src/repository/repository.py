## Import Libries
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.models.Items import ItemBase
from src.configs.create_tables import ItemModel, SessionLocal


## CRUD operations
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


## Add Repositories Functions
def create_item(item: ItemBase, db: Session):

    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return db_item


# Read operation
def read_items(db: Session = None, skip: int = 0, limit: int = 10):

    items = db.query(ItemModel).offset(skip).limit(limit).all()
    return items


def read_item(item_id: int, db: Session = None):

    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


# Update operation
def update_item(item_id: int, item: ItemBase, db: Session = None):

    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    for key, value in item.dict().items():
        setattr(db_item, key, value)

    db.commit()
    db.refresh(db_item)

    return db_item


# Delete operation
def delete_item(item_id: int, db: Session = None):

    item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")

    db.delete(item)
    db.commit()

    return item
