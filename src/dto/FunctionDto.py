from .CommonDto import CommonDto


class FunctionDto(metaclass=CommonDto):
    accuracy: float
    step: float
    range_from: float
    range_to: float
    function: str
    use_template: bool
    use_emissions: bool
