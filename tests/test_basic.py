def add(a: int, b: int) -> int:
    return a + b


# 定义一个测试环境
def test_add():
    result = add(1, 2)
    # 断言实际输出结果为3
    assert result == 3

# uv run pytest -q 自动发现并执行测试
import pytest
from pydantic import ValidationError
from lessons.lesson06 import OrderInput


def test_missing_status():
    data = {
        "order_id": "JP0002",
        "amount": 80,
    }

    with pytest.raises(ValidationError):
        OrderInput.model_validate(data)