import unittest

from car.engine import WilloughbyEngine, SternmanEngine, CapuletEngine


class TestWilloughby(unittest.TestCase):
    def setUp(self):
        self.engine = WilloughbyEngine()

    def test_engine_should_be_serviced(self):
        self.engine.current_mileage = 60001
        self.assertTrue(self.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.engine.current_mileage = 60000
        self.assertFalse(self.engine.needs_service())

class TestSternman(unittest.TestCase):
    def setUp(self):
        self.engine = SternmanEngine()

    def test_engine_should_be_serviced(self):
        self.engine.warning_light_on = True
        self.assertTrue(self.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.engine.warning_light_on = False
        self.assertFalse(self.engine.needs_service())

class TestCapulet(unittest.TestCase):
    def setUp(self):
        self.engine = CapuletEngine()

    def test_engine_should_be_serviced(self):
        self.engine.current_mileage = 30001
        self.assertTrue(self.engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        self.engine.current_mileage = 30000
        self.assertFalse(self.engine.needs_service())
