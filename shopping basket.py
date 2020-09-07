"""
select item...
1: add item
2: remove item
3: showing basket
0: close program
"""

select_item = int(input("""
select item...
1: add item
2: remove item
3: showing basket
0: close program
"""))
shopping_basket = dict()
while select_item != 0:
    if select_item == 1:
        item_name = input("item name: ")
        item_count = int(input("item count: "))
        shopping_basket[item_name] = item_count
    elif select_item == 2:
        remove_item = input('item for remove: ')
        del shopping_basket[remove_item]
    elif select_item == 3:
        for k, v in shopping_basket.items():
            print('{} : {}'.format(k, v))

    select_item = int(input("""
    select item...
    1: add item
    2: remove item
    3: showing basket
    0: close program
    """))
else:
    print('close program')

