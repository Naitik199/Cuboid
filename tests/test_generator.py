import unittest

from buzz import generator

class TestCuboid(unittest.TestCase):
    def test_volume(self):
        self.assertAlmostEqual(generator.cuboid(2),8)
        self.assertAlmostEqual(generator.cuboid(3),27)

    def test_v(self):
        self.assertAlmostEqual(generator.square(2),4)    