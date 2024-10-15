from .abs_auto import AbsAuto


class Toyota(AbsAuto):
    def start(self):
        print("Toyota starts")

    def stop(self):
        print("Toyota stops")
