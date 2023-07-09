from fastapi import APIRouter, Request, Response
from config.dbConnection import client
from models.products_model import Products
from models.orders_model import Orders
from schemas.orders_schema import order_serializer, orders_serializer
from bson import ObjectId

orders_router = APIRouter()

# Fetch List of Orders:
@orders_router.get('/orders')
def get_order(request: Request):
    orders = orders_serializer(request.app.database["orders"].find())
    return {
        "status": "200 OK",
        "data": orders
	}


# Fetch an Order by Id
@orders_router.get('/orders/{id}')
def find_order(request: Request, id: str):
    order = order_serializer(request.app.database["orders"].find_one({"_id": ObjectId(id)}))
    return {
        "status": "200 OK",
        "Order Details": order
	}


# Post an Order
@orders_router.post('/orders')
def create_order(request: Request, order: Orders):
    id = request.app.database["orders"].insert_one(dict(order))
    res = order_serializer(request.app.database["orders"].find_one({"_id": id.inserted_id}))
    return {
        "status": "201 OK",
        "message": "Order Made!",
        "Order Details": res
    }
