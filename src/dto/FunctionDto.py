import typing as T


class FunctionDto:
    accuracy: float
    range_from: float
    range_to: float
    function: str
    use_template: bool
    use_even_range: bool
    use_emissions: bool

    def __init__(self, json: T.Dict[str, T.Any]):
        self.accuracy = json.get('accuracy')
        self.range_from = json.get('range_from')
        self.range_to = json.get('range_to')
        self.function = json.get('function')
        self.use_template = json.get('use_template')
        self.use_even_range = json.get('use_even_range')
        self.use_emissions = json.get('use_emissions')
