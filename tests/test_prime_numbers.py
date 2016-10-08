import unittest
from prime_numbers import get_primes


class PrimeNumbersTest(unittest.TestCase):
    """Test prime_numbers function"""

    def test_first_three_primes(self):
        """Test first three prime numbers"""

        self.assertEqual(get_primes(
            3), [2, 3, 5], msg="First three primes should be [2, 3, 5]")

    def test_first_five_primes(self):
        """Test first five prime numbers"""

        self.assertEqual(get_primes(
            5), [2, 3, 5, 7, 11], msg="First three primes should be [2, 3, 5, 7, 11]")

    def test_for_negative_numbers(self):
        """Raise value error if the input is negative"""

        with self.assertRaises(ValueError):
            get_primes(-3)

    def test_for_non_integers(self):
        """Raise error if the input is not an integer"""

        with self.assertRaises(TypeError):
            get_primes('str')


if __name__ == '__main__':
    unittest.main()