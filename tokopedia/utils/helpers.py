from datetime import datetime
from typing import Union, Optional


def int_to_datetime(value: Union[int, float, None] = None) -> Optional[datetime]:
    if value is None:
        return value
    if isinstance(value, float):
        return datetime.fromtimestamp(value)
    return datetime.fromtimestamp(float(value))
