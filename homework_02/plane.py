"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload

class Plane(Vehicle):
    _cargo: int = 0
    _max_cargo: int = 0

    def __init__(self, weight, fuel, fuel_consumption, max_cargo):
        super().__init__(weight, fuel, fuel_consumption)
        self._max_cargo = max_cargo

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, value):
        self._cargo = value

    @property
    def max_cargo(self):
        return self._max_cargo

    @max_cargo.setter
    def max_cargo(self, value):
        self._max_cargo = value

    def load_cargo(self, value: int):
        if self._cargo + value > self._max_cargo:
            raise CargoOverload
        self._cargo += value

    def remove_all_cargo(self):
        value = self._cargo
        self._cargo = 0
        return value

