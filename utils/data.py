products_data = [
    {
        'code': 'GR1',
        'name': "Green tea",
        'price': 3.11,

    },
    {
        'code': 'SR1',
        'name': "Strawberries",
        'price': 5.00,

    },
    {
        'code': 'CF1',
        'name': "Coffee",
        'price': 11.23,

    },
]

offers_data = [
    {
        'type': 'get_one_free',
        'nth': 2,
        'product': 'GR1',
    },
    {
        'type': 'get_discount',
        'product': 'SR1',
        'nth': 3,
        'discount_amount': 0.5,
    },
    {
        'type': 'get_percent_discount',
        'product': 'CF1',
        'nth': 3,
        'discount_percent': 0.66666667,
    }
]
