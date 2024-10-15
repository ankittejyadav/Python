from .abs_factory import AbsFactory
from chocolates.others import Others


class OthersFactory(AbsFactory):
    def create_chocolate(self):
        self.others = others = Others()
        others.name = "others"
        return others
