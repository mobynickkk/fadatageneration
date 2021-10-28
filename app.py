from flask import Flask

from src import MathServiceInterface


class Application:
    app = Flask(__name__)
    math_service: MathServiceInterface

    @staticmethod
    @app.route('/')
    def index():
        pass


if __name__ == '__main__':
    pass
