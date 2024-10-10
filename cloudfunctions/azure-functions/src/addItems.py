import azure.functions as func
import logging
from sqlalchemy.orm import Session
from configs import ItemModel
bp = func.BluePrints()


@bp.route(route="addItems", auth_level=func.AuthLevel.ANONYMOUS)
def addItems(req: func.HttpRequest, db: Session) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    db_item = db.query(ItemModel).filter(ItemModel.name == name, ItemModel.description == description, ItemModel.price == price, ItemModel.in_stock == in_stock).first()
    if db_item is None:

        db_item = ItemModel()
        db.add(db_item)
        db.commit()
        db.refresh(db_item)

        return {"detail": None, "data": db_item}

    return {"detail": "empty"}

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
