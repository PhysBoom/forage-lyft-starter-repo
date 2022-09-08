from dataclasses import dataclass, field
from typing import List


@dataclass
class Tire:
    """
    Tire (serviced when it needs to be replaced)

    Attributes:
        <float[4]> wear: The tire's wear as measured by the sensors
    """

    wear: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0, 0.0])

    def needs_service(self) -> bool:
        ...

class Carrigan(Tire):
    """
    Carrigan tire (serviced when any of the sensors indicate wear > 0.9)

    Attributes:
        <float[4]> wear: The tire's wear as measured by the sensors
    """

    def needs_service(self) -> bool:
        return any(wear >= 0.9 for wear in self.wear)

class Octoprime(Tire):
    """
    Octoprime tire (serviced when sum(wear) >= 3.0)

    Attributes:
        <float[4]> wear: The tire's wear as measured by the sensors
    """

    def needs_service(self) -> bool:
        return sum(self.wear) >= 3.0
