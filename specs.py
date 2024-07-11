import unittest
from utils.data import products_data, offers_data
from utils.load_data import read_offers, read_products
from cash_register.cash_register import CashRegister

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

class TestBasicCashRegister(unittest.TestCase):
    def test_cash_register_calculation_without_offers(self):
        products = read_products(products_data)
        offers = []

        cart_list = ['GR1', 'SR1', 'CF1']
        cr = CashRegister(products, offers)
    
        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(
            cart_price,
            19.34
        )


    def test_cash_register_get_one_free(self):
        products = read_products(products_data)
        offers = read_offers(offers_data)

        cart_list = ['GR1', 'GR1']
        cr = CashRegister(products, offers)
    
        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(
            cart_price,
            3.11
        )
    
    def test_cash_register_get_discount(self):
        products = read_products(products_data)
        offers = read_offers(offers_data)

        cart_list = ['SR1', 'SR1', 'SR1']
        cr = CashRegister(products, offers)
    
        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(
            cart_price,
            13.5
        )


    def test_cash_register_get_percent_discount(self):
        products = read_products(products_data)
        offers = read_offers(offers_data)

        cart_list = ['CF1', 'CF1', 'CF1']
        cr = CashRegister(products, offers)
    
        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(
            cart_price,
            22.46
        )





if __name__ == '__main__':
    unittest.main()