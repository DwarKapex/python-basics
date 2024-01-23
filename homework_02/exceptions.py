"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""

class CarBaseExeption(Exception):
    pass

class LowFuelError(CarBaseExeption):
    pass

class NotEnoughFuel(CarBaseExeption):
    pass

class CargoOverload(CarBaseExeption):
    pass
