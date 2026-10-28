from lessons.order_types import Order
def find_order_by_id(orders: list[Order], order_id: str) -> Order | None:
    for order in orders:
        if order["order_id"] == order_id:
            return order
    return None

def sum_amount_by_status(orders: list[Order], status: str) -> int:
    total_amount = 0
    for order in orders:
        if order["status"] == status:
            total_amount += order["amount"]
    return total_amount

def count_orders_by_status(orders: list[Order], status: str) -> int:
    count = 0
    for order in orders:
        if order["status"] == status:
            count += 1
    return count
