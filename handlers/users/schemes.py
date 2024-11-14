from pydantic import BaseModel
from annotated_types import Annotated, MaxLen, MinLen


class BaseUser(BaseModel):
    name: Annotated[str, MinLen(2), MaxLen(100)]
    key: Annotated[str, MinLen(10)]


class CreateUser(BaseUser):
    pass
