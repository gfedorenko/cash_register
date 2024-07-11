import unittest
from utils.data import products_data, offers_data
from utils.load_data import read_offers, read_products

class TestDataLoading(unittest.TestCase):
    def test_reading_products_data(self):
        products = read_products(products_data)
        self.assertEqual(
            len(products),
            len(products_data)
        )
    
    def test_reading_offers_data(self):
        offers = read_offers(offers_data)
        self.assertEqual(
            len(offers),
            len(offers_data)
        )




if __name__ == '__main__':
    unittest.main()