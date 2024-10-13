from .abs_auto import AbsAuto


class Toyota(AbsAuto):
    def start(self):
        print("Toyota Starts")

    def stop(self):
        print("Toyota Stops")
