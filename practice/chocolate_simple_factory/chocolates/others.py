from .abs_chocolate import AbsChocolate


class Others(AbsChocolate):
    def __init__(self, chocolate):
        self._chocolate = chocolate

    def eat(self):
        print("I dont like '%s'" % self._chocolate)

    def review(self):
        pass
