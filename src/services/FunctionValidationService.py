import typing as T

from ..dto import FunctionDto
from .ValidationServiceInterface import ValidationServiceInterface


class FunctionValidationService(ValidationServiceInterface):

    def validate(self, dto: T.List[FunctionDto]) -> None:
        # TODO: перенести проверки с ui
        pass
