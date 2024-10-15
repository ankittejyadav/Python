from .abs_auto import AbsAuto


class NullCar(AbsAuto):
    def start(self):
        print('Unknow car "%s"' % (self.name))

    def stop(self):
        pass
