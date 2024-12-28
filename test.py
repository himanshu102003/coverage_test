import unittest
from p1 import is_prime, calculate_fibonacci, sum_of_all_fibonacci

class TestMathFunctions(unittest.TestCase):

    def test_is_prime(self):
        # Test with prime numbers
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))

        # Test with non-prime numbers
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(15))

        # Test with negative numbers
        self.assertFalse(is_prime(-5))
        self.assertFalse(is_prime(-11))

    def test_calculate_fibonacci(self):
        # Test edge cases
        self.assertEqual(calculate_fibonacci(0), 0)
        self.assertEqual(calculate_fibonacci(1), 1)

        # Test for known Fibonacci numbers
        self.assertEqual(calculate_fibonacci(5), 5)
        self.assertEqual(calculate_fibonacci(10), 55)

        # Test with invalid input
        with self.assertRaises(ValueError):
            calculate_fibonacci(-1)

    def test_sum_of_all_fibonacci(self):
        # Test edge cases
        self.assertEqual(sum_of_all_fibonacci(0), 0)
        self.assertEqual(sum_of_all_fibonacci(1), 1)

        # Test for known sums
        self.assertEqual(sum_of_all_fibonacci(5), 12)  # 0 + 1 + 1 + 2 + 3 + 5 = 12
        self.assertEqual(sum_of_all_fibonacci(10), 143)

        # Test with invalid input
        with self.assertRaises(ValueError):
            sum_of_all_fibonacci(-5)

if __name__ == "__main__":
    unittest.main()
