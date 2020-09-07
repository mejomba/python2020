parrot = 'Norwegian Blue'

letter = input("enter a character")

if letter in parrot.casefold():
    print('i find {} in {}'.format(letter, parrot))
else:
    print('i dont find it')

# if letter not in parrot:
#      print('i find {} in {}'.format(letter, parrot))
# else:
#      print('i dont find it')
