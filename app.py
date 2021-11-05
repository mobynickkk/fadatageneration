import typing as T

from flask import Flask, request, render_template, send_from_directory
from src import MathServiceInterface, ValidationServiceInterface, \
    FunctionValidationService, FunctionGraphicService, TaskDto, FunctionDto, IncorrectDataError, CalculationError
from test import MockMathService, MockValidationService


class Application:
    __app = Flask(__name__, template_folder='src/ui/', static_folder='src/ui/')
    math_service: MathServiceInterface
    validation_service: ValidationServiceInterface

    def __init__(self, math_service: MathServiceInterface, validation_service: ValidationServiceInterface):
        self.math_service = math_service
        self.validation_service = validation_service
        self.__static_init(self)

    def run(self, *args, **kwargs):
        self.__app.run(*args, **kwargs)

    @staticmethod
    def __process_json(json_, class_):
        kwargs = dict()
        for k in class_.__annotations__:
            if k in json_:
                kwargs[k] = json_[k]
        return class_(**kwargs)

    @staticmethod
    def __static_init(instance):

        @instance.__app.route('/')
        def index():
            return render_template('index.html')

        @instance.__app.route('/js/<path:path>')
        def send_js(path):
            return send_from_directory('src/ui/js', path)

        @instance.__app.route('/img/<path:path>')
        def send_img(path):
            return send_from_directory('src/ui/img', path)

        @instance.__app.route('/css/<path:path>')
        def send_css(path):
            return send_from_directory('src/ui/css', path)

        @instance.__app.route('/api/', methods=['POST'])
        def api():
            json_ = request.get_json()
            user_id: str = json_['user_id']
            functions: T.List[FunctionDto] = [
                Application.__process_json(obj, FunctionDto) for obj in json_['functions']
            ]
            try:
                instance.validation_service.validate(functions)
                return instance.math_service.run(TaskDto(user_id, functions)).to_json()
            except IncorrectDataError:
                return 'Переданы некорректные данные'
            except CalculationError:
                return 'Ошибка в вычислениях'
            except Exception as e:
                return f'Что-то пошло не так\n\t{e}'


if __name__ == '__main__':
    from sys import argv
    if len(argv) >= 2 and argv[1] == 'test':
        application = Application(MockMathService(), MockValidationService())
        application.run(debug=True)
    else:
        application = Application(FunctionGraphicService(), FunctionValidationService())
        application.run()
