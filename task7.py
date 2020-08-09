def get_max_value(carrot_types, capacity):
    max_val = 0.0
    for ctype in carrot_types:
        factor = int(capacity) / int(ctype['kg'])
        price = int(ctype['price'])
        print(factor)
        c_val = float(factor * price)
        if c_val > max_val:
            max_val = c_val

    print(max_val)


carrotTypes = [{"kg": 5, "price": 100}, {"kg": 7, "price": 150}, {"kg": 3, "price": 70}]

get_max_value(carrotTypes, 30)
