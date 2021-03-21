import attr
from typing import Union


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
