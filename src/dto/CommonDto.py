import json
from dataclasses import dataclass


class CommonDto(type):

    def __new__(mcs, name, bases, dict_):
        result = type(name, (CommonDto.Dto,) + bases, dict_)
        return dataclass(init=True, frozen=True)(result)

    class Dto:

        def to_json(self):
            return json.dumps(vars(self))
