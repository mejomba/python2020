fruit = {
    'black berry': 'شاه توت',
    'pineapple': 'آناناس',
    'raspberry': 'تمشک',
    'grape': 'انگور',
    'olive': 'زیتون',
    'item_key': "item_value"
}
transport = {
    'train': "قطار",
    'ship': "کشتی",
    'car': "ماشین",
    'item_key': "item_value"
}

print(fruit)
print(transport)
print('='*50)
# fruit.update(transport)
# print(fruit)
# print(transport.items())
# for k, v in transport.items():
#     print(k , v)

transport_key = list(transport.keys())
# transport_key.sort()
# for i in transport_key:
#     print('{} : {}'.format(i, transport.get(i)))
# print(transport_key)

# print(list(transport.values()))

# a = dict().fromkeys(transport_key, 'xxx')
# print(a)

# a = transport.pop('train')
# a = transport.popitem()
# print(a)
# print(transport)

# transport_copy = transport.copy()
# print(transport)
# print(transport_copy)

# print(transport.__sizeof__())
# transport.clear()
# print(transport)
# print(transport.__sizeof__())
#
# a = list(range(10000))
# a.clear()
# print(a.__sizeof__())


# print(transport.setdefault('train', 'value'))
# print(transport.get('xxx', 'any'))
# print(transport)


help(int)



