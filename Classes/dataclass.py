from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class Project:
    # name: str  # type hints
    # payment: int
    # client: str
    name: Any
    payment: Any
    client: Any
    # def __init__(self, name, payment, client):
    #     self.name = name
    #     self.payment = payment
    #     self.client = client

    # def __repr__(self):
    #     return f"Project(name={repr(self.name)},payment={repr(self.payment)},client={repr(self.client)})"


class Employee:
    def __init__(self, name, age, salary, project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project


p = Project("ABC", 100, "XYZ")
e = Employee("Ank", 11, 122, p)  # Composition
print(e.project)
