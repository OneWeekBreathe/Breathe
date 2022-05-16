from enum import Enum
from api.resources import strings


class StatusEnum(str, Enum):
    ok = strings.OK
    not_ok = strings.NOT_OK