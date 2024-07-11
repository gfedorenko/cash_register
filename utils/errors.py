class DuplicateProductError(Exception):
    def __init__(self, code):
        super().__init__(f"Product with {code} already exists")

class UnknownItemError(Exception):
    def __init__(self, item):
        super().__init__(f"Item {item} is not in the database")
        