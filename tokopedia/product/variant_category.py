import attr
from typing import List, Optional

from tokopedia.response import TokopediaResponse


@attr.dataclass(slots=True)
class UnitValue:
    value_id: int
    value: str
    hex_code: str
    icon: str


@attr.dataclass(slots=True)
class VariantUnit:
    unit_id: int
    name: str
    short_name: str
    values: List[UnitValue]


@attr.dataclass(slots=True)
class VariantCategory:
    variant_id: int
    name: str
    identifier: str
    status: str
    has_unit: str
    units: List[VariantUnit]


@attr.dataclass(slots=True)
class ResponseVariantCategory(TokopediaResponse):
    data: Optional[List[VariantCategory]]
