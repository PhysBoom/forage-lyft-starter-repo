import time
import unittest

from car.battery import NubbinBattery, SpindlerBattery


class TestNubbin(unittest.TestCase):
    def setUp(self):
        self.battery = NubbinBattery()

    def test_battery_should_be_serviced(self):
        self.battery.last_service_date = int(time.time()) - 365 * 4 * 24 * 60 * 60 - 1
        self.assertTrue(self.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.battery.last_service_date = int(time.time()) - 365 * 3 * 24 * 60 * 60
        self.assertFalse(self.battery.needs_service())

class TestSpindler(unittest.TestCase):
    def setUp(self):
        self.battery = SpindlerBattery()

    def test_battery_should_be_serviced(self):
        self.battery.last_service_date = int(time.time()) - 365 * 3 * 24 * 60 * 60 - 1
        self.assertTrue(self.battery.needs_service())

    def test_battery_should_not_be_serviced(self):
        self.battery.last_service_date = int(time.time()) - 365 * 2 * 24 * 60 * 60
        self.assertFalse(self.battery.needs_service())
