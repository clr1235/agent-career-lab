
# 模拟两条订单数据
orders = [
    {
        "order_id": "JP1001",
        "status": "已签收",
        "amount": 120
    },
    {
        "order_id": "JP1002",
        "status": "运输中",
        "amount": 80
    },
    {
        "order_id": "JP1003",
        "status": "运输中",
        "amount": 200
    }
]

# 遍历订单列表
signed_count = 0
shipping_count = 0
signed_amount = 0
for order in orders:
    # 判断订单是否已签收
    if order["status"] == "已签收":
        signed_count += 1
        signed_amount += order["amount"]
        # 打印符合条件的订单
        print(
            f"订单 {order['order_id']} 已签收，"
            f"金额 {order['amount']} 元"
        )
    elif order["status"] == "运输中":
        shipping_count += 1

print(f"已签收订单数:{signed_count}")
print(f"运输中订单数:{shipping_count}")
print(f"已签收订单总金额:{signed_amount}")