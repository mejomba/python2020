numbers = [1, 5, 65, 32, 41, 20]

for number in numbers:
    if number % 8 == 0:
        print('the number are unacceptable')
        break
else:
    print('the number not found')