from pathlib import Path

from fastapi import FastAPI, HTTPException

from lessons.lesson06 import OrderInput
from lessons.lesson08 import load_orders

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/orders")
def get_orders() -> list[OrderInput]:
    res = load_orders(Path("data/orders.json"))
    return res


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> OrderInput:
    res = load_orders(Path("data/orders.json"))
    for order in res:
        if order.order_id == order_id:
            return order

    raise HTTPException(
        status_code=404,
        detail="订单不存在",
    )
