import math
from collections import defaultdict
from utils.errors import DuplicateProductError, UnknownItemError

offer_funcs = {
    'get_one_free': lambda num, product, offer : math.ceil(
                num/offer.nth
            ) * product.price ,
    'get_discount': lambda num, product, offer  : (
                num * (product.price - offer.discount_amount)
                if num >= offer.nth
                else num * product.price
            ),
    'get_percent_discount': lambda num, product, offer  : (
                num * product.price * offer.discount_percent
                if num >= offer.nth
                else num * product.price
            )
}

class CashRegister:

    def __init__(self, products, offers):
        # use dict for O(1) lookup later on
        self.products = dict()
        for product in products:
            if self.products.get(product.code):
                raise DuplicateProductError(product.code)
            else:
                self.products[product.code] = product
        # assuming we can't have two different offers for one product
        self.offers = {
            offer.product: offer for offer in offers
        }

    def calculate_total_price(self, list):
        sum = 0
        cart = defaultdict(int)
        for item in list:
            if item not in self.products:
                raise UnknownItemError(item)
            cart[item] += 1

        for key, value in cart.items():
            if self.offers.get(key):
                sum += offer_funcs[self.offers[key].type](
                    value,
                    self.products[key],
                    self.offers[key]
                    )
            else:
                sum += self.products[key].price * value
        return round(sum, 2)