from .abs_auto import AbsAuto


class BMW(AbsAuto):
    def start(self):
        print("BMW starts")

    def stop(self):
        print("BMW stops")
