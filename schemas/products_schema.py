def product_serializer(Product) -> dict:
    return {
        "id": str(Product["_id"]),
        "name": Product["name"],
        "price": Product["price"],
        "quantity": Product["quantity"]
	}

def products_serializer(Products) -> list:
    return [product_serializer(Product) for Product in Products]