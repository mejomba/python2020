shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread', 'bread', 'bread', 'bread']

item_to_find = 'spam'
found_at = None


for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        print('spam found at {}'.format(found_at))
        break
else:
    print(f'{item_to_find} not found in shopping list')


# if item_to_find in shopping_list:
#     found_at = shopping_list.index(item_to_find)


