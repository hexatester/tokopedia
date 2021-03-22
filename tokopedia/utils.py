import cattr
from datetime import datetime
from dateutil.parser import parse as parse_datetime
from typing import Any


def make_time(val: None) -> Any:
    if isinstance(val, (int, float)):
        return datetime.fromtimestamp(val)
    if isinstance(val, (str, bytes)):
        return parse_datetime(val)
    return val


def register_hooks():
    cattr.register_structure_hook(datetime, lambda x, t: make_time(x))
