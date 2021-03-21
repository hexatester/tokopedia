import attr
from typing import List, Optional

from tokopedia import TokopediaResponseV2


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
class ResponseProductV2(TokopediaResponseV2):
    data: List[ProductV2]
