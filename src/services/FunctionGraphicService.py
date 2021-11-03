import random

from .MathServiceInterface import MathServiceInterface
from ..dto import TaskDto, CompletedTaskDto


class FunctionGraphicService(MathServiceInterface):

    @staticmethod
    def step_h(range_from, range_to):
        if 1 < abs(range_from - range_to):
            r = random.random() / 10
        else:
            r = abs(range_from - range_to) / (random.random() * 100)
        return r

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        from numpy import arange, sin, cos, e, random, append, savetxt, vstack, delete
        from matplotlib.pyplot import scatter, savefig
        from warnings import filterwarnings

        filterwarnings("ignore", category=FutureWarning)

        for func in dto.functions:
            if func.use_template:
                func.function = func.function.replace('x', '({}*x+{})'.format((0.5 - random.random()) * 10,
                                                                              (0.5 - random.random()) * 10))
                func.function = func.function.replace(func.function,
                                                      '{}*({})+{}'.format((0.5 - random.random()) * 10, func.function,
                                                                          (0.5 - random.random()) * 10))

        main_x = arange(dto.functions[0].range_from, dto.functions[0].range_to,
                        dto.functions[0].step if dto.functions[0].step else FunctionGraphicService.step_h(
                            dto.functions[0].range_from,
                            dto.functions[0].range_to))

        if dto.functions[0].use_emissions:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(dto.functions[0].function.replace('x', str(el)))
                    main_y.append(y + dto.functions[0].accuracy * (0.5 - random.random()))
                except:
                    d.append(ind)
            main_x = delete(main_x, d)
            del d
        else:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(dto.functions[0].function.replace('x', str(el)))
                    main_y.append(y)
                except:
                    d.append(ind)
            main_x = delete(main_x, d)
            del d

        for func in dto.functions[1:]:
            c = main_y[-1] - eval(func.function.replace('x', str(func.range_from)))

            for i in arange(func.range_from, func.range_to,
                            func.step if func.step else FunctionGraphicService.step_h(func.range_from, func.range_to)):

                if func.use_emissions:
                    try:
                        y = eval(func.function.replace('x', str(i))) + c
                        main_x = append(main_x, i)
                        main_y = append(main_y, y + func.accuracy * (0.5 - random.random()))
                    except:
                        pass
                else:
                    try:
                        y = eval(func.function.replace('x', str(i))) + c
                        main_x = append(main_x, i)
                        main_y = append(main_y, y)
                    except:
                        pass

        scatter(main_x, main_y)
        savefig('{}.png'.format(dto.user_id), dpi=100)
        savetxt('{}.csv'.format(dto.user_id), vstack((main_x, main_y)).T, delimiter=',')
        return CompletedTaskDto(['{}.png'.format(dto.user_id), '{}.csv'.format(dto.user_id)])
