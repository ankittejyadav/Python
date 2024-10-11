from dataclasses import dataclass, field
import os
from pathlib import Path


@dataclass
class Phonebook:
    numbers: dict = field(default_factory=dict)

    def __init__(self, temp_dir):
        self.numbers = {}
        self.filename = Path(temp_dir) / "phonebook.txt"
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

    def is_consistent(self):
        for name1, number1 in self.numbers.items():
            for name2, number2 in self.numbers.items():
                if name1 == name2:
                    continue
                if number1.startswith(number2):
                    return False
        return True
