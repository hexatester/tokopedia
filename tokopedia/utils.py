import cattr
from datetime import datetime
from dateutil.parser import parse as parse_datetime


def register_hooks():
    cattr.register_structure_hook(datetime, lambda x, t: parse_datetime(x))
