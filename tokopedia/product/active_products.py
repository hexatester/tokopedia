import attr
from typing import Any, List, Optional

from tokopedia import TokopediaResponse


@attr.dataclass(slots=True)
class ActiveProductsShop:
    id: int
    name: str
    uri: str
    location: str


@attr.dataclass(slots=True)
class ActiveProductShop:
    id: int
    name: str
    url: str
    is_gold: bool
    location: str
    city: str
    reputation: str
    clover: str


@attr.dataclass(slots=True)
class ActiveProductBadge:
    title: str
    image_url: str


@attr.dataclass(slots=True)
class ActiveProduct:
    id: int
    name: str
    childs: Optional[Any]
    url: str
    image_url: str
    image_url_700: str
    price: str
    shop: ActiveProductShop
    wholesale_price: List
    courier_count: int
    condition: int
    category_id: int
    category_name: str
    category_breadcrumb: str
    department_id: int
    labels: List
    badges: List[ActiveProductBadge]
    is_featured: int
    rating: int
    count_review: int
    original_price: str
    discount_expired: str
    discount_percentage: int
    sku: str
    stock: int


@attr.dataclass(slots=True)
class ActiveProducts:
    total_data: int
    shop: ActiveProductsShop
    products: List[ActiveProduct]


@attr.dataclass(slots=True)
class ResponseActiveProducts(TokopediaResponse):
    data: Optional[ActiveProducts] = None
