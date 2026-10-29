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





@pytest.mark.parametrize(
    "data, expected_field, expected_type",
    [
        (
            {
                "order_id": "JP0004",
                "status": "运输中",
                "amount": -50,
            },
            ("amount",),
            "greater_than_equal",
        ),
        (
                {
                    "order_id": "JP0001",
                    "amount": 120
                },
            ("status",),
            "missing",
        ),
        (
                {
                    "order_id": "JP0002",
                    "status": "已签收",
                    "amount": "200"
                },
            ("amount",),
            "int_type"
        ),
        (
                {
                    "order_id": "",
                    "status": "已签收",
                    "amount": 80
                },
            ("order_id",),
            "string_too_short"
        ),
        (
                {
                    "order_id": "JP0003",
                    "status": "",
                    "amount": 100
                },
            ("status",),
            "string_too_short"
        ),
    ],
)
def test_invalid_order(data, expected_field, expected_type):
    with pytest.raises(ValidationError) as exc_info:
        OrderInput.model_validate(data)
    errors = exc_info.value.errors()
    print(errors)
    assert errors[0]["loc"] == expected_field
    assert errors[0]["type"] == expected_type
