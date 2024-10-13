from toyota import Toyota
from mercedes import Mercedes
from bmw import BMW
from nullcar import NullCar

"""Problems - To add a new car, open this code,modify the imports and method -
This Breaks Open/ClosePrinciple

Directly Instatiating car classes - Breaks Dependency Injection Principle

Recognize - Lots of If Else blocks
"""


def get_car(carname):
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
