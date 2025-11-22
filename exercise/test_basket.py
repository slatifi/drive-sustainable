import unittest
from basket import Basket

class TestBasket(unittest.TestCase):
    def setUp (self):
        self.basket = Basket()
    
    def test_add_single_item(self):
        result = self.basket.add_item("apple", 3)
        self.assertTrue(result)
        self.assertEqual(self.basket.items["apple"], 3)

    def test_calculate_price_for_multiple_items(self):
        self.basket.add_item("apple", 2)
        self.basket.add_item("banana", 4)
        total_price = self.basket.calculate_price()
        expected_price = (Basket.item_prices["apple"] * 2) + (Basket.item_prices["banana"] * 4)
        self.assertEqual(total_price, expected_price)

if __name__ == '__main__':
    unittest.main()