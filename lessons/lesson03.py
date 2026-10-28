orders = [
    {"order_id": "JP1001", "status": "已签收", "amount": 120},
    {"order_id": "JP1002", "status": "运输中", "amount": 80},
    {"order_id": "JP1003", "status": "运输中", "amount": 200},
]
orders.append({"order_id": None, "status": "异常数据", "amount": 0})


def find_order_by_id(orders: list[dict], order_id: str) -> dict | None:
    for order in orders:
        if order["order_id"] == order_id:
            return order
    return None


result = find_order_by_id(orders, "JP9999")
if result is None:
    print("未找到订单 JP9999")
else:
    print(result)
print(f"{find_order_by_id(orders, 'JP1001')}")
print(f"{find_order_by_id(orders, 'JP1002')}")
print(f"{find_order_by_id(orders, 'JP1003')}")
assert find_order_by_id(orders, "JP1001") is not None
assert find_order_by_id(orders, "JP9999") is None

invalid_order = {
    "order_id": "JP9998",
    "amount": 50,
}

try:
    invalid_order["status"]
except KeyError:
    print("订单缺少 status 字段")
