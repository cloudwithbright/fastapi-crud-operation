## Import Libries
from fastapi import APIRouter, File, UploadFile
from src.models.Items import ItemBase
from src.service.service import (
    create_item_svc,
    delete_item_svc,
    read_item_svc,
    read_items_svc,
    update_item_svc,
)
import shutil
import os

## Initialize APIRouter
router = APIRouter()


## Add Controllers
@router.get("/")
async def Welcome():
    return {"message": "Endpoint is working. Thank you!"}


@router.post("/items")
async def create_item_cont(item: ItemBase):
    return create_item_svc(item)


# Read operation
@router.get("/items")
async def read_items_cont():
    return read_items_svc()


@router.get("/items/{item_id}")
async def read_item_cont(item_id: int):
    return read_item_svc(item_id)


# Update operation
@router.put("/items/{item_id}")
async def update_item_cont(item_id: int, item: ItemBase):
    return update_item_svc(item_id, item)


# Delete operation
@router.delete("/items/{item_id}")
async def delete_item_cont(item_id: int):
    return delete_item_svc(item_id)

# Define the upload directory
UPLOAD_DIR = "/tmp"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    
    # Create the file path
    file_path = os.path.join(UPLOAD_DIR, file.filename)
        
    # Save the file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    print(os.listdir("/tmp"))
    return {"message": "File uploaded successfully. Thank you!"}
     