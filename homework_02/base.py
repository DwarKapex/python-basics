import numbers
from abc import ABC
from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
)

class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        self._weight = self._validate_int_value(weight)
        self._fuel = self._validate_int_value(fuel)
        self._fuel_consumption = self._validate_int_value(fuel_consumption)
        self._started = False

    def _validate_int_value(self, value):
        if isinstance(value, numbers.Integral):
            return int(value)
        raise TypeError("number is not integral")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = self._validate_int_value(value)

    @property
    def fuel(self):
        return self._fuel

    @fuel.setter
    def fuel(self, value):
        self._fuel = self._validate_int_value(value)

    @property
    def fuel_consumption(self):
        return self._fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, value):
        self._fuel_consumption = self._validate_int_value(value)

    @property
    def started(self):
        return self._started

    @started.setter
    def started(self, value):
        self._started = bool(value)

    def start(self):
        if not self._started and self._fuel <= 0:
            raise LowFuelError("low on fuel")
        self._started = True

    def move(self, distance):
        if distance * self._fuel_consumption > self._fuel:
            raise NotEnoughFuel
        self._fuel -= distance * self._fuel_consumption
