import pytest

from lessons.lesson06 import OrderInput
from pydantic import ValidationError


def test_valid_order():
    data = {
        "order_id": "JP0001",
        "status": "已签收",
        "amount": 120,
    }

    order = OrderInput.model_validate(data)

    assert order.order_id == "JP0001"
    assert order.amount == 120

def test_missing_status():
    data = {
        "order_id": "JP0002",
        "amount": 80,
    }

    with pytest.raises(ValidationError):
        OrderInput.model_validate(data)