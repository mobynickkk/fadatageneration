import typing as T

from ..exceptions import IncorrectDataError
from ..dto import FunctionDto
from .ValidationServiceInterface import ValidationServiceInterface


class FunctionValidationService(ValidationServiceInterface):
    restricted_words = ['import', 'compile', 'eval', 'exec', 'try', 'except', 'return', 'def', 'class', 'type',
                        'dir', 'dict', 'list', 'tuple', 'while', 'for', ' in', 'range', 'yield', 'async', 'await',
                        'lambda']

    def validate(self, dto: T.List[FunctionDto]) -> None:
        for function_dto in dto:
            self.check(function_dto)

    def check(self, entity: FunctionDto) -> None:
        self.__check_fields(entity)
        self.__check_range(entity)
        self.__check_function(entity)

    @staticmethod
    def __check_fields(entity: FunctionDto):
        if entity.accuracy <= 0 or len(entity.function) == 0 or entity.step <= 0:
            raise IncorrectDataError()

    @staticmethod
    def __check_range(entity: FunctionDto) -> None:
        if entity.range_to <= entity.range_from or (entity.range_to - entity.range_from) <= entity.step:
            raise IncorrectDataError()

    def __check_function(self, entity: FunctionDto) -> None:
        for word in self.restricted_words:
            if word in entity.function:
                raise IncorrectDataError()
