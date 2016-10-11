import unittest
from drink_class import Alcohol, Beverage


class TestDrinkClass(unittest.TestCase):

    def test_beverage_instance(self):
        tea = Beverage("Tea", 100)
        self.assertIsInstance(
            tea, Beverage, msg="The object should be an instance of the `Beverage` class")

    def test_alcohol_instance(self):
        tusker = Alcohol("Tusker", "beer", 100)
        self.assertIsInstance(
            tusker, Alcohol, msg="The object should be an instance of the `Alcohol` class")

    def test_beverage_price(self):
        tea = Beverage("Tea", 100)
        self.assertEqual(tea.price(), 1000,
                         msg="Price when volume = 100 should 1000 ")

    def test_alcohol_price(self):
        tusker = Alcohol("Tusker", "beer", 100, 2)
        self.assertEqual(tusker.price(), 2000,
                         msg="Alcohol price should be 2000 ")

    def test_drink_alcohol(self):
        tusker = Alcohol("Tusker", "beer", 100, 2)
        self.assertEqual(tusker.drink(50), 'Cheers! You have 50 units of Tusker left',
                         msg="Alcohol volume should be should be 50 ")

    def test_drink_beverage(self):
        tea = Beverage("Tea", 100)
        self.assertEqual(tea.drink(100), 'Cheers! You have 0 units of Tea left',
                         msg="Beverage volume should be should be 0 ")
