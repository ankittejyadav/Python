"""AbstactClass"""

import abc


class MyABC(abc.ABC):

    @abc.abstractmethod
    def do_something(self, value=None):
        """Method"""

    @abc.abstractproperty
    def some_property(self):
        """Property"""


# Interface
class MyClass(MyABC):

    def __init__(self, value=None):
        self._myprop = value

    def do_something(self):
        self._myprop *= value

    @property
    def some_property(self):
        return self._myprop


# Incorrect Interface
class BadClass(MyABC):
    pass

    bad = BadClass()
