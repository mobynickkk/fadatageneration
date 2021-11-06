import random
import numpy as np
import matplotlib.pyplot as plt

from .MathServiceInterface import MathServiceInterface
from ..exceptions import IncorrectDataError
from ..dto import FunctionDto, TaskDto, CompletedTaskDto


class FunctionGraphicService(MathServiceInterface):

    @staticmethod
    def step_h(range_from: float, range_to: float) -> float:
        return random.random() / 10 \
            if 1 < abs(range_from - range_to) \
            else abs(range_from - range_to) / (random.random() * 100)

    @staticmethod
    def __save_data(x: np.ndarray, y: np.ndarray, dto: TaskDto):
        plt.scatter(x, y)
        plt.savefig(f'src/ui/tmp/{dto.user_id}.png', dpi=100)
        np.savetxt(f'src/ui/tmp/{dto.user_id}.csv', np.vstack((x, y)).T, delimiter=',')
        return CompletedTaskDto(f'{dto.user_id}.csv', f'{dto.user_id}.png')

    @staticmethod
    def __get_function(function_dto: FunctionDto):
        try:
            return eval('lambda x: ' + function_dto.function)
        except Exception:
            raise IncorrectDataError(f'Ошибка при попытке расчета функции {function_dto.function}')

    @staticmethod
    def __get_factor(val: float = 10.) -> float:
        return (0.5 - random.random()) * val

    def __calc_first_function(self, function_dto: FunctionDto, main_x: np.ndarray) -> (np.ndarray, np.ndarray):
        main_y = []
        d = []

        func = self.__get_function(function_dto)

        for ind, el in enumerate(main_x):
            try:
                y = func(el)
                main_y.append(y + self.__get_factor(function_dto.accuracy)
                              if function_dto.use_emissions
                              else y)
            except Exception:
                d.append(ind)

        main_x = np.delete(main_x, d)
        del d
        return main_x, main_y

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        from warnings import filterwarnings

        filterwarnings("ignore", category=FutureWarning)

        for function_dto in dto.functions:
            if function_dto.use_template:
                function_dto.function = function_dto.function.replace(
                    'x', f'({self.__get_factor()}*x+{self.__get_factor()})')
                function_dto.function = function_dto.function.replace(
                    function_dto.function, f'{self.__get_factor()}*({function_dto.function})+{self.__get_factor()}')

        main_x, main_y = self.__calc_first_function(dto.functions[0],
                                                    np.arange(dto.functions[0].range_from, dto.functions[0].range_to,
                                                              dto.functions[0].step
                                                              if dto.functions[0].step
                                                              else self.step_h(dto.functions[0].range_from,
                                                                               dto.functions[0].range_to))
                                                    )

        for function_dto in dto.functions[1:]:
            func = self.__get_function(function_dto)
            c = main_y[-1] - func(function_dto.range_from)

            step = function_dto.step \
                if function_dto.step \
                else self.step_h(function_dto.range_from, function_dto.range_to)

            for i in np.arange(function_dto.range_from, function_dto.range_to, step):
                try:
                    y = func(i) + c
                    main_x = np.append(main_x, i)
                    main_y = np.append(main_y,
                                       y + self.__get_factor(function_dto.accuracy)
                                       if function_dto.use_emissions
                                       else y)
                except Exception:
                    continue

        return self.__save_data(main_x, main_y, dto)
