from toyota import Toyota
from mercedes import Mercedes
from bmw import BMW
from nullcar import NullCar
from typing import Union

"""Problems - To add a new car, open this code,modify the imports and method -
This Breaks Open/Close Principle

Directly Instatiating car classes - Breaks Dependency Injection Principle

Recognize - Lots of If Else blocks
"""


def get_car(carname: str) -> Union[Toyota, Mercedes, BMW, NullCar]:
    if carname == "Toyota":
        return Toyota()
    elif carname == "Mercedes":
        return Mercedes()
    elif carname == "BMW":
        return BMW()
    else:
        """Null Pattern - Returns a dummy instance that still implements all the required methods
        No need to test null objects at runtime"""
        return NullCar(carname)


for carname in "Toyota", "Mercedes", "BMW", "Vroom":
    car = get_car(carname)
    car.start()
    car.stop()
