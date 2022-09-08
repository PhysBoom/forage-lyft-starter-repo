from abc import ABC

from car.serviceable import Serviceable


class Engine:
    def needs_service(self) -> bool:
        ...


class CapuletEngine(Engine):
    """
    Capulet engine (serviced every 30,000 miles)

    Attributes:
        last_service_mileage: mileage at last service
        current_mileage: current mileage
    """

    def __init__(self, last_service_mileage: int = 0, current_mileage: int = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 30000


class WilloughbyEngine(Engine):
    """
    Willoughby engine (serviced every 60,000 miles)

    Attributes:
        last_service_mileage: mileage at last service
        current_mileage: current mileage
    """

    def __init__(self, last_service_mileage: int = 0, current_mileage: int = 0):
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000


class SternmanEngine(Engine):
    """
    Sternman engine (serviced when warning light is on)

    Attributes:
        warning_light_on: Whether the warning light is on
    """

    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
        return self.warning_light_on
