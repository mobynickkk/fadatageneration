from ..dto import TaskDto, CompletedTaskDto


class MathServiceInterface:

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        """
        Метод, производящий необходимые вычисления над переданными функциями
        :param dto: дто с функциями для вычислений
        :return: расположение графика в формате картинки и csv файла с точками для аппроксимации
        """
        raise NotImplementedError('This is interface method')
