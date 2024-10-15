from inspect import getmembers, isclass, isabstract
import chocolates


class ChocolateFactory(object):
    chocolates = {}

    def __init__(self):
        self.load_chocolates()

    def load_chocolates(self):
        classes = getmembers(chocolates, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, chocolates.AbsChocolate):
                self.chocolates.update([[name, _type]])

    def create_instance(self, chocolate):
        if chocolate in self.chocolates:
            return self.chocolates[chocolate]()
        else:
            return chocolates.Others(chocolate)
