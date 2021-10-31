import typing as T

from .CommonDto import CommonDto
from .FunctionDto import FunctionDto


class TaskDto(metaclass=CommonDto):
    user_id: str
    functions: T.List[FunctionDto]
