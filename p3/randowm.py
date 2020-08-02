import random

secret = random.randint(1,10)
temp = input('input a number:')
guess = int(temp)
times = 1

while (guess != secret) and (times < 3):
    if guess > secret:
        print('lower')
    else:
        print('lower')
        
    temp = input('again:')
    guess = int(temp)
    times = times+1

if (guess == secret) and (times <= 3):
    print('correct')
else:
    print('The opportunity is exhausted')