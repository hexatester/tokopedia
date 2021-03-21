import attr
from datetime import datetime
from typing import Dict, List, Optional, Union

from tokopedia import TokopediaResponse
from tokopedia.utils.helpers import int_to_datetime


@attr.dataclass(slots=True)
class ProductBasic:
    productID: int
    shopID: int
    status: int
    name: str
    condition: int
    childCategoryID: int
    shortDesc: str


@attr.dataclass(slots=True)
class ProductPrice:
    value: int
    currency: int
    idr: int
    LastUpdateUnix: Optional[datetime]


@attr.dataclass(slots=True)
class ProductWeight:
    value: int
    unit: int


@attr.dataclass(slots=True)
class ProductStock:
    value: int
    stockWording: str


@attr.dataclass(slots=True)
class ProductVariant:
    isParent: bool
    isVariant: bool
    childrenID: List[int] = attr.ib(factory=list)


@attr.dataclass(slots=True)
class ProductMenu:
    id: int
    name: str


@attr.dataclass(slots=True)
class ProductExtraAttribute:
    minOrder: int
    lastUpdateCategory: int
    isEligibleCOD: bool


@attr.dataclass(slots=True)
class ProductWholesale:
    price: ProductPrice
    minQuantity: int
    maxQuantity: int


@attr.dataclass(slots=True)
class ProductCategory:
    id: int
    name: str
    title: str
    breadcrumbURL: str


@attr.dataclass(slots=True)
class ProductPicture:
    picID: int
    fileName: str
    filePath: str
    status: int
    OriginalURL: str
    ThumbnailURL: str
    width: int
    height: int
    URL300: str


@attr.dataclass(slots=True)
class ProductGMStats:
    transactionSuccess: int
    transactionReject: int
    countSold: int


@attr.dataclass(slots=True)
class ProductStats:
    countView: int


@attr.dataclass(slots=True)
class ProductOther:
    sku: str
    url: str
    mobileURL: str


@attr.dataclass(slots=True)
class ProductCampaign:
    StartDate: str
    EndDate: str


@attr.dataclass(slots=True)
class ProductWarehouseStock:
    useStock: bool
    value: int


@attr.dataclass(slots=True)
class ProductWarehouse:
    productID: int
    warehouseID: int
    price: ProductPrice
    stock: ProductWarehouseStock


@attr.dataclass(slots=True)
class Product:
    basic: ProductBasic
    price: ProductPrice
    weight: ProductWeight
    stock: ProductStock
    main_stock: int
    reserve_stock: int
    variant: ProductVariant
    menu: Union[ProductMenu, Dict]
    preorder: Dict
    extraAttribute: ProductExtraAttribute
    wholesale: Optional[ProductWholesale]
    categoryTree: List[ProductCategory]
    pictures: List[ProductPicture]
    GMStats: Union[ProductGMStats, Dict]
    stats: Union[ProductStats, Dict]
    other: ProductOther
    campaign: ProductCampaign
    warehouses: List[ProductWarehouse]


class ResponseProduct(TokopediaResponse[Product]):
    data: List[Product]
