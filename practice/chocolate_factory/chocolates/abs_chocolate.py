import abc


class AbsChocolate(abc.ABC):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @abc.abstractmethod
    def eat(self):
        pass

    @abc.abstractmethod
    def review(self):
        pass
