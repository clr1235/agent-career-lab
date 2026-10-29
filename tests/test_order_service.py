from lessons.order_data import orders
from lessons.order_service import (
    count_orders_by_status,
    find_order_by_id,
    sum_amount_by_status,
)


def test_count_orders_by_status():
    result = count_orders_by_status(orders, "已签收")
    assert result == 1


def test_find_existing_order():
    result = find_order_by_id(orders, "JP1001")
    assert result["order_id"] == "JP1001"


def test_find_missing_order():
    result = find_order_by_id(orders, "JP9999")
    assert result is None


def test_count_shipping_orders():
    result = count_orders_by_status(orders, "运输中")
    assert result == 2


def test_sum_shipping_amount():
    result = sum_amount_by_status(orders, "运输中")
    assert result == 280


def test_count_missing_status():
    result = count_orders_by_status(orders, "已取消")
    assert result == 0
