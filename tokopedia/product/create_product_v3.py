import attr
from enum import Enum
from typing import List, Optional

from tokopedia import TokopediaResponse


@attr.dataclass(slots=True)
class ProductV3Wholesale:
    min_qty: int
    price: int


@attr.dataclass(slots=True)
class ProductV3Picture:
    file_path: str


@attr.dataclass(slots=True)
class ProductV3Video:
    url: str
    source: str
    type: str


@attr.dataclass(slots=True)
class ProductV3Etalase:
    id: int


@attr.dataclass(slots=True)
class ProductV3Dimension:
    height: int
    width: int
    length: int


@attr.dataclass(slots=True)
class ProductV3Preorder:
    is_active: bool
    duration: int
    time_unit: str


@attr.dataclass(slots=True)
class ProductV3Variant:
    variant: int
    product_variant: int


class ProductV3Currency(Enum):
    IDR = "IDR"
    USD = "USD"


class ProductV3Status(Enum):
    UNLIMITED = "UNLIMITED"
    LIMITED = "LIMITED"
    EMPTY = "EMPTY"


class ProductV3WeightUnit(Enum):
    GR = "GR"
    KG = "KG"


class ProductV3Condition(Enum):
    NEW = "NEW"
    USED = "USED"


@attr.dataclass(slots=True)
class CreateProductV3:
    name: str
    category_id: int
    price_currency: ProductV3Currency
    price: int
    status: ProductV3Status
    min_order: int
    weight: float
    weight_unit: ProductV3WeightUnit
    condition: ProductV3Condition
    dimension: Optional[ProductV3Dimension] = None
    custom_product_logistics: Optional[List[int]] = None
    annotations: Optional[List[str]] = None
    etalase: Optional[ProductV3Etalase] = None
    description: Optional[str] = None
    is_must_insurance: Optional[bool] = None
    is_free_return: Optional[bool] = None
    sku: Optional[str] = None
    stock: Optional[int] = None
    wholesale: Optional[List[ProductV3Wholesale]] = None
    preorder: Optional[List[ProductV3Preorder]] = None
    pictures: Optional[List[ProductV3Picture]] = None
    videos: Optional[List[ProductV3Video]] = None
    variant: Optional[List[ProductV3Variant]] = None


@attr.dataclass(slots=True)
class FailedData:
    product_name: str
    product_price: int
    sku: str
    error: List[str]


@attr.dataclass(slots=True)
class SuccessData:
    product_id: int


@attr.dataclass(slots=True)
class ResponseCreateProductV3:
    total_data: int
    success_data: int
    fail_data: int
    success_rows_data: Optional[List[SuccessData]] = None
    failed_rows_data: Optional[List[FailedData]] = None


@attr.dataclass(slots=True)
class ResponsesCreateProductV3(TokopediaResponse):
    data: ResponseCreateProductV3
