import typing as T

from .FunctionDto import FunctionDto


class TaskDto:
    functions: T.List[FunctionDto]

    def __init__(self, json: T.List[T.Dict[str, T.Any]]):
        self.functions = [FunctionDto(el) for el in json]
