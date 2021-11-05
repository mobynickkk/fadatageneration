import random
import numpy as np
import matplotlib.pyplot as plt

from .MathServiceInterface import MathServiceInterface
from ..exceptions import CalculationError
from ..dto import TaskDto, CompletedTaskDto


class FunctionGraphicService(MathServiceInterface):

    @staticmethod
    def step_h(range_from: float, range_to: float) -> float:
        return random.random() / 10 \
            if 1 < abs(range_from - range_to) \
            else abs(range_from - range_to) / (random.random() * 100)

    @staticmethod
    def __save_data(x: np.ndarray, y: np.ndarray, dto: TaskDto):
        plt.scatter(x, y)
        plt.savefig(f'{dto.user_id}.png', dpi=100)
        np.savetxt(f'{dto.user_id}.csv', np.vstack((x, y)).T, delimiter=',')
        return CompletedTaskDto(f'{dto.user_id}.csv', f'{dto.user_id}.png')

    @staticmethod
    def get_factor() -> float:
        return (0.5 - random.random()) * 10

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        from warnings import filterwarnings

        filterwarnings("ignore", category=FutureWarning)

        for func in dto.functions:
            if func.use_template:
                func.function = func.function.replace('x', f'({self.get_factor()}*x+{self.get_factor()})')
                func.function = func.function.replace(func.function,
                                                      f'{self.get_factor()}*({func.function})+{self.get_factor()}')

        main_x = np.arange(dto.functions[0].range_from, dto.functions[0].range_to,
                           dto.functions[0].step
                           if dto.functions[0].step
                           else self.step_h(dto.functions[0].range_from, dto.functions[0].range_to))

        if dto.functions[0].use_emissions:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(dto.functions[0].function.replace('x', str(el)))
                    main_y.append(y + dto.functions[0].accuracy * (0.5 - random.random()))
                except Exception:
                    d.append(ind)
            main_x = np.delete(main_x, d)
            del d
        else:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(dto.functions[0].function.replace('x', str(el)))
                    main_y.append(y)
                except Exception:
                    d.append(ind)
            main_x = np.delete(main_x, d)
            del d

        for func in dto.functions[1:]:
            c = main_y[-1] - eval(func.function.replace('x', str(func.range_from)))
            step = func.step if func.step else self.step_h(func.range_from, func.range_to)

            for i in np.arange(func.range_from, func.range_to, step):
                if func.use_emissions:
                    try:
                        y = eval(func.function.replace('x', str(i))) + c
                        main_x = np.append(main_x, i)
                        main_y = np.append(main_y, y + func.accuracy * (0.5 - random.random()))
                    except Exception:
                        raise CalculationError()
                else:
                    try:
                        y = eval(func.function.replace('x', str(i))) + c
                        main_x = np.append(main_x, i)
                        main_y = np.append(main_y, y)
                    except Exception:
                        raise CalculationError()

        return self.__save_data(main_x, main_y, dto)
