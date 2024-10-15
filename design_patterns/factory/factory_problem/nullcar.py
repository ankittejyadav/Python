from dataclasses import dataclass
from typing import Self


@dataclass(slots=True)
class NullCar(object):
    # def __init__(self, carname):
    #     self._carname = carname
    _carname: str

    def start(self: Self) -> None:
        print('Unknown car "%s"' % self._carname)

    def stop(self: Self) -> None:
        pass
