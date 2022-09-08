from abc import ABC, abstractmethod


class Serviceable(ABC):
    @property
    @abstractmethod
    def needs_service(self) -> bool:
        ...
