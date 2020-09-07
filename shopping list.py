shopping_list = ['milk', 'pasta', 'eggs', 'spam', 'bread']

# for item in shopping_list:
#     if item != 'spam':
#         print(f'by {item}')
#

for item in shopping_list:
    if item == 'spam':
        break

    print(f'by {item}')