def order_serializer(Order) -> dict:
    return {
        "id": str(Order["_id"]),
        "timestamp": Order["timestamp"],
        "items": Order["items"],
        "address": Order["address"]
	}


def orders_serializer(Orders) -> list:
    return [order_serializer(Order) for Order in Orders]