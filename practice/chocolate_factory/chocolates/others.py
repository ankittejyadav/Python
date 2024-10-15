from .abs_chocolate import AbsChocolate


class Others(AbsChocolate):
    # def __init__(self, chocolate):
    #     self._chocolate = chocolate

    def eat(self):
        print("I dont like '%s'" % (self.name))

    def review(self):
        pass
