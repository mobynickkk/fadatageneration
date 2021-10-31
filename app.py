from flask import Flask, request
from src import MathServiceInterface, TaskDto
import json


class Application:
    __app = Flask(__name__)
    math_service: MathServiceInterface

    def __init__(self, service: MathServiceInterface):
        self.math_service = service
        self.__static_init(self)

    def run(self, *args, **kwargs):
        self.__app.run(*args, **kwargs)

    @staticmethod
    def __static_init(instance):

        @instance.__app.route('/')
        def index():
            return 'Welcome page'

        @instance.__app.route('/api', methods=['POST'])
        def api():
            # TODO: сделать проверки
            return instance.math_service.run(TaskDto(json.loads(request.get_json())))


if __name__ == '__main__':
    application = Application(None)
    application.run()
