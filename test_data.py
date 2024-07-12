duplicate_products_data = [
    {
        'code': 'GR1',
        'name': "Green tea",
        'price': 3.11,

    },
    {
        'code': 'GR1',
        'name': "Green tea",
        'price': 3.11,

    },
]

updated_products_data = [
    {
        'code': 'GR1',
        'name': "Green tea",
        'price': 3.00,

    },
    {
        'code': 'SR1',
        'name': "Strawberries",
        'price': 5.00,

    },
    {
        'code': 'CF1',
        'name': "Coffee",
        'price': 12.00,

    },
]

updated_offers_data = [
    {
        'type': 'get_one_free',
        'nth': 4,
        'product': 'SR1',
    },
    {
        'type': 'get_discount',
        'product': 'GR1',
        'nth': 5,
        'discount_amount': 1,
    },
    {
        'type': 'get_percent_discount',
        'product': 'CF1',
        'nth': 5,
        'after_discount_percent': 0.5,
    }
]
unknown_offer_data = [
    {
        'type': 'unknown',
        'nth': 4,
        'product': 'SR1',
    },
]


