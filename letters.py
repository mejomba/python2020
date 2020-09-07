#          01234567890123456789012345
letters = 'abcdefghijklmnopqrstuvwxyz'

backwards = letters[::-1]
print(backwards)

# qpo
print(letters[16:13:-1])
# edcba
print(letters[4::-1])
# last 8 character in reverse order
print(letters[:-9:-1])


print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])


a = (1,2,3,4)
b = (1,2,3,4)
print(a + b)