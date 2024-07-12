class Offer:

    def __init__(self, type, product, nth, discount_amount=0, after_discount_percent=0):
        self.type = type
        self.product = product
        self.nth = nth
        self.discount_amount = discount_amount
        self.after_discount_percent = after_discount_percent
