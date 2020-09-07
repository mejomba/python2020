import random

highest = 1000
answer = random.randint(1, highest)
print(answer) # TODO remove after testing

print('یه عدد بین 1 تا {} حدث بزن: '.format(highest))
guess = 0
while guess != answer:
    guess = input()

    if guess.lower() == 'quit':
        break
    if int(guess) == answer:
        print('افرین درست حدث زدی')
        break
    elif int(guess) > answer:
        print('یه عدد کوچیک تر حدث بزن')
    else:
        print('یه عدد بزرگتر حدث بزن')
