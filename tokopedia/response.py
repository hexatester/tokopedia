import attr
from typing import Generic, TypeVar, Union


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


T = TypeVar("T")


@attr.dataclass(slots=True)
class TokopediaResponse(Generic[T]):
    header: Union[ResponseHeader, ErrorResponseHeader, None]
    data: T
