from dataclasses import dataclass

from car.battery import Battery
from car.engine import Engine
from car.serviceable import Serviceable


@dataclass
class Car(Serviceable):
    """
    Car (serviced when either the engine or battery needs servicing)

    Attributes:
        engine: The car's engine
        battery: The car's battery
    """
    engine: Engine
    battery: Battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()
