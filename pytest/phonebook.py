from dataclasses import dataclass, field
import os


@dataclass
class Phonebook:
    numbers: dict = field(default_factory=dict)

    def __init__(self):
        self.numbers = {}
        self.filename = "phonebook.txt"
        self.cache = open(self.filename, "w")

    def add_empty(self, name: str, number: str) -> None:
        pass

    def lookup_empty(self, name: str) -> str:
        pass

    def add(self, name: str, number: str) -> None:
        self.numbers[name] = number

    def lookup(self, name: str) -> str:
        return self.numbers[name]

    def all_names(self):
        return set(self.numbers.keys())

    def clear(self):
        self.cache.close()
        os.remove(self.filename)
