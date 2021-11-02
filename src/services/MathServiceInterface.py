from ..dto import TaskDto, CompletedTaskDto


class MathServiceInterface:

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        """
        Метод, производящий необходимые вычисления над переданными функциями
        :param dto: дто с функциями для вычислений
        :return: расположение графика в формате картинки и csv файла с точками для аппроксимации
        """
        raise NotImplementedError('This is interface method')
        from numpy import arange, sin, cos, e, random, append, savetxt, vstack, delete
        from matplotlib.pyplot import scatter, savefig
        from warnings import filterwarnings
        filterwarnings("ignore", category=FutureWarning)
        def step_h(range_from,range_to):
            
            if 1 < abs(range_from-range_to):
                r = random.random()/10
            else:
                r = abs(range_from-range_to)/(random.random()*100)
            return r
        
        
        for func in data.functions:
            if func.use_template :
                func.function = func.function.replace('x','({}*x+{})'.format((0.5 - random.random())*10,(0.5 - random.random())*10))
                func.function = func.function.replace(func.function, '{}*({})+{}'.format((0.5 - random.random())*10,func.function,(0.5 - random.random())*10))
        
        main_x = arange(data.functions[0].range_from, data.functions[0].range_to,data.functions[0].step if data.functions[0].step else step_h(data.functions[0].range_from, data.functions[0].range_to))
        
        if data.function[0].use_emissions:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(data.funtions[0].function.replace('x',str(el)))
                    main_y.append(y + data.functions[0].accuracy*(0.5-random.random()))
                except:
                    d.append(ind)
            main_x = delete(main_x, d)
            del d
        else:
            main_y = []
            d = []
            for ind, el in enumerate(main_x):
                try:
                    y = eval(data.funtions[0].function.replace('x',str(el)))
                    main_y.append(y)
                except:
                    d.append(ind)
            main_x = delete(main_x, d)
            del d 
        

        for func in data.functions[1:]:
            c = main_y[-1] - eval(func.function.replace('x', func.range_from))
            
            for i in arange(func.range_from, func.range_to, func.step if func.step else step_h(data.functions[0].range_from, data.functions[0].range_to)):
                
                if func.use_emissions:
                    try:
                        y = eval(func.function.replace('x', str(i)))
                        main_x = append(main_x, i)
                        main_y = append(main_y, y + func.accuracy*(0.5-random.random()))
                    except:
                        pass
                else:
                    try:
                        y = eval(func.function.replace('x', str(i)))
                        main_x = append(main_x, i)
                        main_y = append(main_y, y)
                    except:
                        pass

        scatter(main_x,main_y)
        savefig('{}.png'.format(data.user_id), dpi = 100)
        savetxt('{}.csv'.format(data.user_id),vstack((main_x,main_y)).T, delimiter=',')
        return ['{}.png'.format(data.user_id),'{}.csv'.format(data.user_id)]
