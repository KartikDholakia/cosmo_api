from pydantic import BaseModel

class Products(BaseModel):
    name: str
    price: float
    quantity: int = 1