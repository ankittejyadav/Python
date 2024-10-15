from .abs_factory import AbsFactory
from chocolates.mars import Mars


class MarsFactory(AbsFactory):
    def create_chocolate(self):
        self.mars = mars = Mars()
        mars.name = "Mars"
        return mars
