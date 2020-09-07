# parrot = 'Norwegian Blue'
#
# for character in parrot:
#     print(character)


number = '123.512:45"5412>555;'
seperator = ''
num = ''

for char in number:
    if not char.isnumeric():
        seperator = seperator + char
    else:
        num = num + char

print(seperator)
print(num)
