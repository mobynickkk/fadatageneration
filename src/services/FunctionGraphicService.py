from .MathServiceInterface import MathServiceInterface
from ..dto import TaskDto, CompletedTaskDto


class FunctionGraphicService(MathServiceInterface):

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        pass
