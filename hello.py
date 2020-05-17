#hello


def discaunted(price, discount, max_discount=55):
    price = abs(float(price))
    discount = abs(float(discount))
    max_discount = abs(float(max_discount))
    if max_discount > 99:
        raise ValueError('To mach discount')
    if discount >= max_discount:
        price_with_discount = price
    else:
        price_with_discount = price - (price / 100 * discount)
    return price_with_discount


print(discaunted(100000,50))



