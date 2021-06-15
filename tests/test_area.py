import os, sys
new_path = os.path.dirname(os.getcwd())
sys.path.append(new_path+ "/scripts")
import unittest
from math import pi
from circles import circles_area

class TestCircleArea(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(circles_area(1), pi)
        self.assertAlmostEqual(circles_area(0), 0)
