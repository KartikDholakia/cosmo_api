from fastapi import APIRouter, Request, Response
from config.dbConnection import client
from models.products_model import Products
from schemas.products_schema import product_serializer, products_serializer
from bson import ObjectId

products_router = APIRouter()

# Fetch List of Products
@products_router.get('/products')
async def get_products(request: Request):
    products = products_serializer(request.app.database["products"].find())
    return {
        "status": "200 OK",
        "data": products
	}


# Create a new Product:
@products_router.post('/products')
async def new_product(request: Request, product: Products):
    id = request.app.database["products"].insert_one(dict(product))
    print(id.inserted_id)
    res = product_serializer(request.app.database["products"].find_one({"_id": id.inserted_id}))
    print(res)
    return {
        "status": "201 OK",
        "message": "Product added!",
        "Product": res
    }


# Update a product
@products_router.put('/products/{id}')
async def update_product(request: Request, id: str, product: Products):
    request.app.database["products"].find_one_and_update(
        {"_id": ObjectId(id)},
        {"$set": dict(product)}
    )

    updated_product = product_serializer(request.app.database["products"].find_one({"_id": ObjectId(id)}))

    return {
        "status": "200 OK",
        "message": "Product details updated",
        "updated product": updated_product
    }