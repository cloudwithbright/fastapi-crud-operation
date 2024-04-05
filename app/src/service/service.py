from src.models.Items import ItemBase
from src.repository.repository import (
    create_item,
    delete_item,
    read_item,
    read_items,
    update_item,
    get_db
)

## Add Repositories Functions
def create_item_svc(item: ItemBase):

    db = next(get_db())
    return create_item(item, db)


# Read operation
def read_items_svc():

    db = next(get_db())
    return read_items(db)


def read_item_svc(item_id: int):
    
    db = next(get_db())
    return read_item(item_id, db)


# Update operation
def update_item_svc(item_id: int, item: ItemBase):

    db = next(get_db())
    return update_item(item_id, item, db)


# Delete operation
def delete_item_svc(item_id: int):

    db = next(get_db())
    return delete_item(item_id, db)
