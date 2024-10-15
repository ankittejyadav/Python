from inspect import getmembers, isclass, isabstract
import autos

"""Dynamic Loading: The factory automatically loads all the concrete car classes from the autos module 
when it is instantiated.
Instance Creation: The create_instance() method can be used to create objects of any car model that is 
defined in the autos module and that inherits from AbsAuto."""


class AutoFactory(object):
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return autos.NullCar(carname)
