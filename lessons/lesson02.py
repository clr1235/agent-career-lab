orders = [
    {"order_id": "JP1001", "status": "已签收", "amount": 120},
    {"order_id": "JP1002", "status": "运输中", "amount": 80},
    {"order_id": "JP1003", "status": "运输中", "amount": 200},
]


# 订单数量统计函数
def count_orders_by_status(orders: list[dict], status: str) -> int:
    count = 0
    for order in orders:
        if order["status"] == status:
            count += 1
    return count


print(f"已签收：{count_orders_by_status(orders, '已签收')}")
print(f"运输中：{count_orders_by_status(orders, '运输中')}")
print(f"已取消：{count_orders_by_status(orders, '已取消')}")


def sum_amount_by_status(orders: list[dict], status: str) -> int:
    total_amount = 0
    for order in orders:
        if order["status"] == status:
            total_amount += order["amount"]
    return total_amount


print(f"已签收：{sum_amount_by_status(orders, '已签收')}")
print(f"运输中：{sum_amount_by_status(orders, '运输中')}")
print(f"已取消：{sum_amount_by_status(orders, '已取消')}")
