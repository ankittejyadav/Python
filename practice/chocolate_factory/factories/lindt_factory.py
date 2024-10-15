from .abs_factory import AbsFactory
from chocolates.lindt import Lindt


class LindtFactory(AbsFactory):
    def create_chocolate(self):
        self.lindt = lindt = Lindt()
        lindt.name = "Lindt"
        return lindt
