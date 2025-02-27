import time

from car.battery import SpindlerBattery, NubbinBattery
from car.car import Car
from car.engine import CapuletEngine, WilloughbyEngine, SternmanEngine


def create_calliope(
    current_date: int = int(time.time()),
    last_service_date: int = int(time.time()),
    last_service_mileage: int = 0,
    current_mileage: int = 0,
) -> Car:
    return Car(
        CapuletEngine(last_service_mileage, current_mileage),
        SpindlerBattery(last_service_date, current_date),
    )


def create_glissade(
    current_date: int = int(time.time()),
    last_service_date: int = int(time.time()),
    last_service_mileage: int = 0,
    current_mileage: int = 0,
) -> Car:
    return Car(
        WilloughbyEngine(last_service_mileage, current_mileage),
        SpindlerBattery(last_service_date, current_date),
    )


def create_palindrome(
    current_date: int = int(time.time()),
    last_service_date: int = int(time.time()),
    warning_light_on: bool = False,
) -> Car:
    return Car(
        SternmanEngine(warning_light_on),
        SpindlerBattery(last_service_date, current_date),
    )


def create_rorschach(
    current_date: int = int(time.time()),
    last_service_date: int = int(time.time()),
    last_service_mileage: int = 0,
    current_mileage: int = 0,
) -> Car:
    return Car(
        WilloughbyEngine(last_service_mileage, current_mileage),
        NubbinBattery(last_service_date, current_date),
    )


def create_thovex(
    current_date: int = int(time.time()),
    last_service_date: int = int(time.time()),
    last_service_mileage: int = 0,
    current_mileage: int = 0,
) -> Car:
    return Car(
        CapuletEngine(last_service_mileage, current_mileage),
        NubbinBattery(last_service_date, current_date),
    )
