import attr
from typing import List, Optional

from tokopedia import TokopediaResponse


@attr.dataclass(slots=True)
class VariantOption:
    id: int
    value: str
    hex: str


@attr.dataclass(slots=True)
class Variant:
    name: str
    identifier: str
    unit_name: str
    position: int
    option: List[VariantOption]


@attr.dataclass(slots=True)
class VariantChildrenPicture:
    original: str
    thumbnail: str


@attr.dataclass(slots=True)
class VariantChildrenCampaign:
    is_active: bool
    discounted_percentage: int
    discounted_price: int
    discounted_price_fmt: str
    campaign_type: int
    campaign_type_name: str
    start_date: str
    end_date: str


@attr.dataclass(slots=True)
class VariantChildren:
    name: str
    url: str
    product_id: int
    price: int
    price_fmt: str
    stock: int
    main_stock: int
    sku: str
    option_ids: List[int]
    enabled: bool
    is_buyable: bool
    is_wishlist: bool
    picture: VariantChildrenPicture
    campaign: VariantChildrenCampaign
    always_available: bool
    stock_wording: str
    other_variant_stock: str
    is_limited_stock: bool
    reserve_stock: Optional[int] = None


@attr.dataclass(slots=True)
class VariantProduct:
    parent_id: int
    default_child: int
    sizechart: str
    variant: List[Variant]
    children: List[VariantChildren]


@attr.dataclass(slots=True)
class ResponseVariantProduct(TokopediaResponse):
    data: Optional[VariantProduct]
