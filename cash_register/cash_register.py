import math
from collections import defaultdict

class CashRegister:

    def __init__(self, products, offers):
        # use dict for O(1) lookup later on
        self.products = {
            product.code: product
            for product in products
        }
        # assuming we can't have two different offers for one product
        self.offers = {
            offer.product: offer for offer in offers
        }

    def calculate_total_price(self, list):
        sum = 0
        cart = defaultdict(int)
        for item in list:
            cart[item] += 1

        for key, value in cart.items():
            sum += self.products[key].price * value
        return round(sum, 2)