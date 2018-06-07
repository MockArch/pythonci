import unittest
from src.math import Math


class MathTest(unittest.TestCase):

    def test_addition(self):
        # Make test fail
        self.assertEqual(Math.addition(3, 4), 8)



def run_test():
	unittest.main(verbosity=2)