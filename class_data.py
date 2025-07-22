import json

with open('data.json', encoding='utf-8') as file:
    dict = json.load(file)


class Data:
    def __init__(self) -> None:
        self.slovar = dict

    def data(self, key: str) -> str:
        return self.slovar.get(key)
