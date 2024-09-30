## Import Packages
from pydantic import BaseModel

# Pydantic models
class ItemBase(BaseModel):
    name: str
    description: str
    price: float
    in_stock: bool

class Item(ItemBase):
    id: int