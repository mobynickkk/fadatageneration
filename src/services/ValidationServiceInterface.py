import typing as T


class ValidationServiceInterface:

    def validate(self, dto: T.Any) -> None:
        """
        Метод, проверяющий дто на корректность
        и вызывающий в случае неправильных данных ошибку <src.exceptions.IncorrectDataError>
        :param dto: дто для проверки
        """
        raise NotImplementedError('Not implemented')
