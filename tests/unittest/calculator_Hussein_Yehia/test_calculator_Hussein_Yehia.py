import sys
import os
import unittest


# Add the src/main/python directory to the path.
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../../../src/main/python'
)))

from calculator_Hussein_Yehia import add, subtract, multiply, divide


class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)

        with self.assertRaises(ValueError):
            divide(10, 0)


if __name__ == "__main__":
    unittest.main()
