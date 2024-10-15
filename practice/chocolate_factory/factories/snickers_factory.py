from .abs_factory import AbsFactory
from chocolates.snickers import Snickers


class SnickersFactory(AbsFactory):
    def create_chocolate(self):
        self.snickers = snickers = Snickers()
        snickers.name = "Snickers"
        return snickers
