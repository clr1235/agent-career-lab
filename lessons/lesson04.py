from lessons.order_data import orders
from lessons.order_service import (count_orders_by_status, sum_amount_by_status, find_order_by_id)

def main():
    # 在这里调用你的业务函数
    print(f"JP1001 订单状态：{find_order_by_id(orders, 'JP1001')["status"]}")
    result = find_order_by_id(orders, "JP9999")
    if result is None:
        print("JP9999 订单不存在")

    print(f"已签收：{count_orders_by_status(orders, '已签收')}")
    print(f"运输中：{count_orders_by_status(orders, '运输中')}")
    print(f"已取消：{count_orders_by_status(orders, '已取消')}")
    print(f"已签收：{sum_amount_by_status(orders, '已签收')}")
    print(f"运输中：{sum_amount_by_status(orders, '运输中')}")
    print(f"已取消：{sum_amount_by_status(orders, '已取消')}")

if __name__ == "__main__":
    main()