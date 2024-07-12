from utils.load_data import read_offers, read_products
from utils.data import products_data, offers_data
from cash_register.cash_register import CashRegister


if __name__ == "__main__":

    products = read_products(products_data)
    offers = read_offers(offers_data)

    cash_register = CashRegister(products, offers)

    str = input("List of products in the cart: ")
    cart = str.split(" ")
    total = cash_register.calculate_total_price(cart)
    print(f"Your total: {total}")
