from pydantic import BaseModel
from datetime import datetime
from models.products_model import Products
from typing import List


class Address(BaseModel):
    city: str
    country: str
    zip_code: int


class Items(BaseModel):
    product_id: str
    quantity: int


class Orders(BaseModel):
    timestamp: datetime = datetime.now()
    items: List[Items]
    address: Address