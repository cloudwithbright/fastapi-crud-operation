from src.models.Items import ItemBase
from src.repository.repository import (
    create_item,
    delete_item,
    read_item,
    read_items,
    update_item,
    get_db,
)


## Add Repositories Functions
def create_item_svc(item: ItemBase):

    db = next(get_db())
    response = create_item(item, db)
    return (
        {
            "message": "Item added successfully. Thank you!",
            "data": [response["data"]],
        }
        if response["detail"] == None
        else {"message": "Item exists. Thank you!", "data": []}
    )


## Read operation
def read_items_svc():

    db = next(get_db())
    response = read_items(db)

    return (
        {"message": "Item found. Thank you!", "data": response["data"]}
        if response["detail"] == None
        else {"message": "No Item found. Thank you!", "data": []}
    )


def read_item_svc(item_id: int):

    db = next(get_db())
    response = read_item(item_id, db)

    return (
        {"message": "Item found. Thank you!", "data": [response]}
        if response != None
        else {"message": "Item not found. Thank you!", "data": []}
    )


# Update operation
def update_item_svc(item_id: int, item: ItemBase):

    db = next(get_db())
    response = update_item(item_id, item, db)

    return (
        {"message": "Item updated successfully. Thank you!", "data": [response["data"]]}
        if (response["detail"] == None)
        else {"message": "Item not found. Thank you!", "data": []}
    )


# Delete operation
def delete_item_svc(item_id: int):

    # db = next(get_db())
    db = next(get_db())
    response = delete_item(item_id, db)
    return (
        {
            "message": "Item deleted successfully. Thank you!",
            "data": [response["data"]],
        }
        if response["detail"] != "empty"
        else {"message": "Item not found. Thank you!", "data": []}
    )
