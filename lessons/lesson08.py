import json
from pathlib import Path
from lessons.lesson06 import OrderInput


def load_orders(file_path: Path) -> list[OrderInput]:
    result = []
    # 由你自己实现
    with file_path.open("r", encoding="utf-8") as file:
        orders = json.load(file)
        for order in orders:
            valid_order = OrderInput.model_validate(order)
            result.append(valid_order)
    return result


def main() -> None:
    try:
        res = load_orders(Path("data/orders.json"))
        for order in res:
            print(f"订单编号:{order.order_id} {order.status} {order.amount}")
    except FileNotFoundError:
        print("文件不存在")
    except json.JSONDecodeError:
        print("json格式错误")


if __name__ == "__main__":
    main()
