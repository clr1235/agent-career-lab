from pydantic import BaseModel, Field, ValidationError


class OrderInput(BaseModel):
    order_id: str = Field(min_length=1, max_length=50)
    status: str = Field(min_length=1, max_length=50)
    amount: int = Field(strict=True, ge=0)

if __name__ == '__main__':
    test_data = [
        {"order_id": "", "status": "已签收", "amount": 120},
        {"order_id": "JP0002","amount": 80},
        {"order_id": "JP0003", "status": "", "amount": "200"},
        {"order_id": "JP0004", "status": "运输中", "amount": -50}
    ]
    for data in test_data:
        try:
            order = OrderInput.model_validate(data)
            print(order.model_dump())
        except ValidationError as e:
            for error in e.errors():
                print(f"字段{error["loc"]}：{error['msg']}")