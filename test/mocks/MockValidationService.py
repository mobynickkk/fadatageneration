import typing as T

from src import ValidationServiceInterface


class MockValidationService(ValidationServiceInterface):

    def validate(self, dto: T.Any) -> None:
        return
