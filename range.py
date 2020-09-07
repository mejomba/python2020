
my_list = list(range(10))
print(my_list)

# even = list(range(0, 100, 2))
# odd = list(range(1, 100, 2))
# print(even)
# print(odd)
#
small_decimals = range(0, 10)
# print(small_decimals)
#
# for i in small_decimals:
#     print(i)
# my_range = small_decimals[::-1]
# print(my_range)
# for i in my_range:
#     print(i)

x = int(input('enter a number between 1, 1000: '))
sevens = list(range(7, 1000, 7))
if x in sevens:
    print(f'{x} in sevens')
else:
    print('not found')

