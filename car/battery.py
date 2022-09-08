import time


class Battery:
    def needs_service(self) -> bool:
        ...


class SpindlerBattery(Battery):
    """
    The Spindler Battery (serviced every two years).

    Attributes:
        last_service_date: The date of the last service (UNIX)
        current_date: The current date (UNIX)
    """

    def __init__(
        self,
        last_service_date: int = int(time.time()),
        current_date: int = int(time.time()),
    ):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 365 * 3 * 24 * 60 * 60


class NubbinBattery(Battery):
    """
    The Nubbin Battery (serviced every four years).

    Attributes:
        last_service_date: The date of the last service (UNIX)
        current_date: The current date (UNIX)
    """

    def __init__(
        self,
        last_service_date: int = int(time.time()),
        current_date: int = int(time.time()),
    ):
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return self.current_date - self.last_service_date >= 365 * 4 * 24 * 60 * 60
