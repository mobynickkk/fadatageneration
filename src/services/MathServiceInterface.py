from ..dto import TaskDto, CompletedTaskDto


class MathServiceInterface:

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        raise NotImplementedError('This is interface method')
