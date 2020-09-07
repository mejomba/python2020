low = 1
high = 1000

print('یه عدد بین {} و {} در نظر بگیرید'.format(low, high))

guesses = 1

while True:
    guess = low + (high - low) // 2
    # print('i guesses between range {} to {}'.format(low, high))
    high_low = input('my guess is {} , is correct or lower or higher '.format(guess)).casefold()

    if high_low == 'h':
        low = guess + 1
    elif high_low == 'l':
        high = guess - 1
    elif high_low == 'c':
        print('i got it {}'.format(guess))
        break

    guesses = guesses + 1

print(guesses)
