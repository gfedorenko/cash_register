import unittest
from utils.data import products_data, offers_data
from test_data import (
    duplicate_products_data,
    updated_products_data,
    updated_offers_data,
    unknown_offer_data,
)
from utils.load_data import read_offers, read_products
from cash_register.cash_register import CashRegister
from utils.errors import DuplicateProductError, UnknownItemError, UnknownOfferTypeError


class TestDataLoading(unittest.TestCase):
    def setUp(self):
        self.products = read_products(products_data)
        self.offers = read_offers(offers_data)

    def test_reading_products_data(self):
        self.assertEqual(len(self.products), len(products_data))

    def test_reading_offers_data(self):
        self.assertEqual(len(self.offers), len(offers_data))


class TestBasicCashRegister(unittest.TestCase):
    def setUp(self):
        self.products = read_products(products_data)
        self.offers = read_offers(offers_data)

    def test_cash_register_calculation_without_offers(self):
        offers = []

        cart_list = ["GR1", "SR1", "CF1"]
        cr = CashRegister(self.products, offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 19.34)

    def test_cash_register_get_one_free(self):
        cart_list = ["GR1", "GR1"]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 3.11)

    def test_cash_register_get_discount(self):
        cart_list = ["SR1", "SR1", "SR1"]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 13.5)

    def test_cash_register_get_percent_discount(self):
        cart_list = ["CF1", "CF1", "CF1"]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 22.46)

    def test_cash_register_duplicated_item(self):
        products = read_products(duplicate_products_data)
        with self.assertRaises(DuplicateProductError):
            CashRegister(products, self.offers)

    def test_cash_register_unknown_item(self):
        cr = CashRegister(self.products, self.offers)

        cart_list = ["UNK", "CF1", "CF1"]
        with self.assertRaises(UnknownItemError):
            cr.calculate_total_price(cart_list)

    def test_cash_register_unknown_offer(self):
        offers = read_offers(unknown_offer_data)

        with self.assertRaises(UnknownOfferTypeError):
            CashRegister(self.products, offers)


# Test different parameters for offers
class TestCashRegisterEditedOffers(unittest.TestCase):
    def setUp(self):
        self.products = read_products(updated_products_data)
        self.offers = read_offers(updated_offers_data)

    def test_cash_register_get_one_free(self):
        cart_list = ["SR1", "SR1", "SR1", "SR1"]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 15)

    def test_cash_register_discount(self):
        cart_list = ['GR1', 'GR1', 'GR1', 'GR1', 'GR1',]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 10)

    def test_cash_register_discount_precent(self):
        cart_list = ["CF1", "CF1", "CF1", "CF1", "CF1", "CF1"]
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 36)

    def test_cash_register_get_one_free(self):
        cart_list = ['GR1', 'GR1', 'GR1', 'GR1', 'GR1', 'GR1',
                     'SR1', 'SR1', 'SR1', 'SR1', 'SR1',
                     'CF1', 'CF1', 'CF1', 'CF1', 'CF1', 'CF1', 'CF1']
        cr = CashRegister(self.products, self.offers)

        cart_price = cr.calculate_total_price(cart_list)
        self.assertEqual(cart_price, 74)


if __name__ == "__main__":
    unittest.main()
