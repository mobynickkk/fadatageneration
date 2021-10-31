import typing as T

from flask import Flask, request
from src import MathServiceInterface, TaskDto, FunctionDto
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
            json_ = json.loads(request.get_json())
            user_id: str = json_['user_id']
            functions: T.List[FunctionDto] = json_['functions']
            # TODO: сделать проверки
            try:
                return instance.math_service.run(TaskDto(user_id, functions)).to_json()
            except Exception as e:
                return f'Something went wrong due to {e}'


if __name__ == '__main__':
    application = Application(None)
    application.run()
