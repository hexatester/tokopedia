import attr
from typing import List, Optional, Union


@attr.dataclass(slots=True)
class BaseResponseHeader:
    process_time: float
    messages: str


class ResponseHeader(BaseResponseHeader):
    pass


@attr.dataclass(slots=True)
class ErrorResponseHeader(BaseResponseHeader):
    reason: str
    error_code: str


@attr.dataclass(slots=True)
class TokopediaResponse:
    header: Union[ResponseHeader, ErrorResponseHeader, None]


@attr.dataclass(slots=True)
class TokopediaResponseV2:
    status: Optional[str]
    error_message: Optional[List[str]]
