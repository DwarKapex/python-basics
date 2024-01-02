import numbers
from pydantic import BaseModel, StrictBool, NonNegativeInt
from abc import ABC
from homework_02.exceptions import (
    LowFuelError,
    NotEnoughFuel,
)


class Vehicle(ABC, BaseModel):
    # force pydantic to validate values on assignment
    class Config:
        validate_assignment = True

    weight: NonNegativeInt
    fuel: NonNegativeInt
    fuel_consumption: NonNegativeInt
    started: StrictBool

    def __init__(self, weight=0, fuel=0, fuel_consumption=0):
        # pydantic does not support positional initialization from the box
        # so need to pass the values of args directly
        super().__init__(weight=weight, fuel=fuel, fuel_consumption=fuel_consumption, started=False)

    def start(self):
        if not self.started and self.fuel <= 0:
            raise LowFuelError("low on fuel")
        self.started = True

    def move(self, distance):
        if distance * self.fuel_consumption > self.fuel:
            raise NotEnoughFuel
        self.fuel -= distance * self.fuel_consumption
