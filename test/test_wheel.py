import unittest

from car.tire import Carrigan, Octoprime


class TestCarrigan(unittest.TestCase):
    def setUp(self):
        self.wheel = Carrigan()

    def test_needs_servicing(self):
        self.wheel.wear[1] = 0.9
        self.assertTrue(self.wheel.needs_service())

    def test_does_not_need_servicing(self):
        self.wheel.wear[1] = 0.8
        self.assertFalse(self.wheel.needs_service())

class TestOctoprime(unittest.TestCase):
    def setUp(self):
        self.wheel = Octoprime()

    def test_needs_servicing(self):
        self.wheel.wear = [1, 1, 0.5, 0.5]
        self.assertTrue(self.wheel.needs_service())

    def test_does_not_need_servicing(self):
        self.wheel.wear = [0.5, 0.5, 0.5, 0.5]
        self.assertFalse(self.wheel.needs_service())
