"""
создайте класс `Car`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.engine import Engine


class Car(Vehicle):
    _engine = Engine()

    @property
    def engine(self):
        return self._engine

    def set_engine(self, value):
        if not isinstance(value, Engine):
            raise TypeError("Wrong type for engine")
        self._engine = value
