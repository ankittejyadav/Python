from .abs_auto import Abs_Auto


class NullCar(Abs_Auto):

    def start(self):
        print('Unknow car "%s"' % (self.name))

    def stop(self):
        pass
