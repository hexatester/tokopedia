import attr
from typing import List, Optional


@attr.dataclass(slots=True)
class ProductV2:
    product_id: int
    name: str
    sku: str
    shop_id: int
    shop_name: str
    category_id: int
    desc: str
    stock: int
    price: int
    status: str


@attr.dataclass(slots=True)
class ResponseProductV2:
    data: List[ProductV2] = attr.ib(factory=list)
    status: Optional[str] = None
    error_message: Optional[List[str]] = None
