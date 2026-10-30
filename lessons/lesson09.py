import json
from pathlib import Path
from lessons.lesson06 import OrderInput
from lessons.lesson08 import load_orders


def save_orders(
    file_path: Path,
    orders: list[OrderInput],
) -> None:
    temp_path = file_path.with_suffix(".tmp")
    result = [order.model_dump() for order in orders]
    json_str = json.dumps(result, ensure_ascii=False, indent=2)
    temp_path.write_text(
        json_str,
        encoding="utf-8",
    )
    temp_path.replace(file_path)


def main() -> None:
    file_path = Path("data/orders.json")
    orders = load_orders(file_path)
    # 以下是OrderInput的两种创建方式
    new_order = OrderInput(
        order_id="JP1004",
        status="待发货",
        amount=500,
    )
    # data = {
    #     "order_id": "JP1004",
    #     "status": "待发货",
    #     "amount": 500,
    # }
    # new_order = OrderInput.model_validate(data)

    orders.append(new_order)
    save_orders(Path("data/orders_updated.json"), orders)
    saved_orders = load_orders(Path("data/orders_updated.json"))
    assert len(saved_orders) == 4
    assert any(
        order.order_id == "JP1004" and order.amount == 500 for order in saved_orders
    )
    assert any(order.order_id == "JP1001" for order in saved_orders)
    assert any(order.order_id == "JP1002" for order in saved_orders)
    assert any(order.order_id == "JP1003" for order in saved_orders)


if __name__ == "__main__":
    main()
