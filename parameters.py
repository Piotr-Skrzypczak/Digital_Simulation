import json
from pprint import PrettyPrinter
from types import SimpleNamespace


class Parameters(SimpleNamespace):
    def __init__(self, text: str = "{}", file_name: str = None):
        if file_name is None:
            data = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))
        else:
            with open(file_name, "r") as file:
                data = json.load(file, object_hook=lambda d: SimpleNamespace(**d))

        super().__init__(**data.__dict__)