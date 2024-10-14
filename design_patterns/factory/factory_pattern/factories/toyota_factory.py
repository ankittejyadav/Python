from .abs_factory import AbsFactory
from autos.toyota import Toyota


class ToyotaFactory(AbsFactory):
    def create_auto(self):
        self.toyota = toyota = Toyota()
        toyota.name = "Toyota"
        return toyota
