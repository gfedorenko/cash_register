from utils.load_data import read_offers, read_products
from utils.data import products_data, offers_data


if __name__ == '__main__':

    products = read_products(products_data)
    offers = read_offers(offers_data)

    print(products, offers)