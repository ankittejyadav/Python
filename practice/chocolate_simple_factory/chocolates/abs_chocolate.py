import abc


class AbsChocolate(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def review(self):
        pass
