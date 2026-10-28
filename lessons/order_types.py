from typing import TypedDict


class Order(TypedDict):
    order_id: str
    status: str
    amount: int
