from pathlib import Path

from fastapi import FastAPI, HTTPException

from lessons.lesson06 import OrderInput
from lessons.lesson08 import load_orders
from lessons.lesson09 import save_orders

app = FastAPI()

ORDERS_FILE = Path("data/orders_api.json")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/orders")
def get_orders() -> list[OrderInput]:
    res = load_orders(ORDERS_FILE)
    return res


@app.get("/orders/{order_id}")
def get_order(order_id: str) -> OrderInput:
    res = load_orders(ORDERS_FILE)
    for order in res:
        if order.order_id == order_id:
            return order

    raise HTTPException(
        status_code=404,
        detail="订单不存在",
    )


@app.post("/orders", status_code=201)
def create_order(order: OrderInput) -> OrderInput:
    # 1. 读取已有订单
    orders = load_orders(ORDERS_FILE)
    # 2. 检查 order_id 是否重复
    for item in orders:
        if item.order_id == order.order_id:
            raise HTTPException(status_code=409, detail="订单编号已存在")
    # 3. 将新订单添加到列表
    orders.append(order)
    # 4. 保存全部订单
    save_orders(ORDERS_FILE, orders)
    # 5. 返回新订单
    return order
