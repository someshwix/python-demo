import unittest
from dummy import add_numbers

class TestAddNumbers(unittest.TestCase):

    def test_add_positive_numbers(self):
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_positive_and_negative_numbers(self):
        self.assertEqual(add_numbers(3, -5), -2)

    def test_add_zero(self):
        self.assertEqual(add_numbers(0, 0), 0)
        self.assertEqual(add_numbers(3, 0), 3)
        self.assertEqual(add_numbers(0, 5), 5)

if __name__ == "__main__":
    unittest.main()