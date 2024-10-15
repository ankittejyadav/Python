import abc


class AbsFactory(abc.ABC):

    @abc.abstractmethod
    def create_chocolate(self):
        pass
