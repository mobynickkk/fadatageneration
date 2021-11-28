from src import MathServiceInterface, TaskDto, CompletedTaskDto


class MockMathService(MathServiceInterface):

    def run(self, dto: TaskDto) -> CompletedTaskDto:
        return CompletedTaskDto(
            'test/resources/test.csv',
            'test/resources/test.jpg'
        )
