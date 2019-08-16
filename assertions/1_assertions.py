def apply_discount(product, discount):
    price = int(product['price'] * (1.0 - discount))
    assert 0 <= price <= product['price']
    return price


shoes = {'name': 'shoes', 'price': 12000}

print(apply_discount(shoes, .12))
print(apply_discount(shoes, 2))
