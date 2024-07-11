from cash_register.product import Product
from cash_register.offer import Offer

def read_products(products_data):
    products = []
    for item in products_data:
        products.append(Product(
            item['code'],
            item['name'],
            item['price']
            ))

    return products

def read_offers(offers_data):
    offers = []
    for item in offers_data:
        offers.append(Offer(
            item['type'],
            item['product'],
            item['nth'],
            discount_amount=item.get('discount_amount', 0),
            discount_percent=item.get('discount_percent', 0)
            ))

    return offers