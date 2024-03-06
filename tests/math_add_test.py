import unittest

from src.math import add


class MathTestCase(unittest.TestCase):
    # Test case 1
    def test_add_positive_numbers(self):
        self.assertEqual(add(3, 4), 7)

    # Test case 2
    def test_add_negative_numbers(self):
        self.assertEqual(add(-3, -4), -7)

    # Test case 3
    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -5), -3)


if __name__ == '__main__':
    unittest.main()
