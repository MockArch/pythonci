import unittest
from src.math import Math


class MathTest(unittest.TestCase):

    def test_addition(self):
        # Make test fail
        c = Math()
        self.assertEqual(c.addition(4, 4), 9)
