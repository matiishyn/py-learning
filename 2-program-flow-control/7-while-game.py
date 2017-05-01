import random

highest = 10
answer = random.randint(1, highest)

guess = ''

while guess != answer:
    guess = int(input('Guess an int number in [1,10):'))
    if guess < answer:
        print('Guess higher')
    elif guess > answer:
        print('Guess lower')
    else:
        print('{} is a correct answer'.format(guess))
