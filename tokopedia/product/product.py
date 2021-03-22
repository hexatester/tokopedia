import attr
from datetime import datetime
from typing import Dict, List, Optional

from tokopedia import TokopediaResponse


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
    stockWording: Optional[str] = None
    useStock: Optional[bool] = None


@attr.dataclass(slots=True)
class ProductVariant:
    isParent: Optional[bool] = None
    isVariant: Optional[bool] = None
    childrenID: List[int] = attr.ib(factory=list)


@attr.dataclass(slots=True)
class ProductMenu:
    id: int
    name: str


@attr.dataclass(slots=True)
class ProductExtraAttribute:
    minOrder: int
    lastUpdateCategory: int
    isEligibleCOD: Optional[bool] = None


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
    transactionSuccess: Optional[int] = None
    transactionReject: Optional[int] = None
    countSold: Optional[int] = None


@attr.dataclass(slots=True)
class ProductStats:
    countView: Optional[int] = None


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


@attr.dataclass(slots=True, kw_only=True)
class Product:
    basic: ProductBasic
    price: ProductPrice
    weight: ProductWeight
    stock: ProductStock
    main_stock: int
    reserve_stock: Optional[int] = None
    variant: ProductVariant
    menu: ProductMenu
    preorder: Dict
    extraAttribute: ProductExtraAttribute
    wholesale: Optional[ProductWholesale] = None
    categoryTree: List[ProductCategory]
    pictures: List[ProductPicture]
    GMStats: ProductGMStats
    stats: ProductStats
    other: ProductOther
    campaign: ProductCampaign
    warehouses: List[ProductWarehouse]


@attr.dataclass(slots=True)
class ResponseProduct(TokopediaResponse):
    data: Optional[List[Product]]
