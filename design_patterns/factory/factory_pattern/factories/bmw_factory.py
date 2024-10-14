from .abs_factory import AbsFactory
from autos.bmw import BMW


class BMWFactory(AbsFactory):
    def create_auto(self):
        self.bmw = bmw = BMW()
        self.name = "BMW"
        return bmw
