import time
import unittest

from car.car_factory import (
    create_calliope,
    create_glissade,
    create_palindrome,
    create_rorschach,
    create_thovex,
)


class TestCalliope(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = create_calliope(
            last_service_date=int(time.time()) - 365 * 2 * 24 * 60 * 60 - 1
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = create_calliope(
            last_service_date=int(time.time()) - 365 * 1 * 24 * 60 * 60
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = create_calliope(current_mileage=30001)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = create_calliope(current_mileage=30000)
        self.assertFalse(car.needs_service())


class TestGlissade(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = create_glissade(
            last_service_date=int(time.time()) - 365 * 2 * 24 * 60 * 60 - 1
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = create_glissade(
            last_service_date=int(time.time()) - 365 * 1 * 24 * 60 * 60
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = create_glissade(current_mileage=60001)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = create_glissade(current_mileage=60000)
        self.assertFalse(car.needs_service())


class TestPalindrome(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = create_palindrome(
            last_service_date=int(time.time()) - 365 * 2 * 24 * 60 * 60 - 1
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = create_palindrome(
            last_service_date=int(time.time()) - 365 * 1 * 24 * 60 * 60
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = create_palindrome(warning_light_on=True)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = create_palindrome(warning_light_on=False)
        self.assertFalse(car.needs_service())


class TestRorschach(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = create_rorschach(
            last_service_date=int(time.time()) - 365 * 4 * 24 * 60 * 60 - 1
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = create_rorschach(
            last_service_date=int(time.time()) - 365 * 3 * 24 * 60 * 60
        )
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = create_rorschach(current_mileage=60001)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = create_rorschach(current_mileage=60000)
        self.assertFalse(car.needs_service())


class TestThovex(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        car = create_thovex(
            last_service_date=int(time.time()) - 365 * 4 * 24 * 60 * 60 - 1
        )
        self.assertTrue(car.needs_service())

    def test_battery_should_not_be_serviced(self):
        car = create_thovex(last_service_date=int(time.time()) - 365 * 3 * 24 * 60 * 60)
        self.assertFalse(car.needs_service())

    def test_engine_should_be_serviced(self):
        car = create_thovex(current_mileage=30001)
        self.assertTrue(car.needs_service())

    def test_engine_should_not_be_serviced(self):
        car = create_thovex(current_mileage=30000)
        self.assertFalse(car.needs_service())


if __name__ == "__main__":
    unittest.main()
