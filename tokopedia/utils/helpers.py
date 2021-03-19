from datetime import datetime
from typing import Union


def int_to_datetime(value: Union[int, float]) -> datetime:
    if isinstance(value, float):
        return datetime.fromtimestamp(value)
    return datetime.fromtimestamp(float(value))
