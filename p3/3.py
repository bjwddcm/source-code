import random

secret = random.randint(1,10)
temp = input('input a number:')
guess = int(temp)
time = 1

while (guess != secret) and (time < 3):
    if guess > secret:
        print('lower')
    else:
        print('higher')
    
    temp = input('again:')
    guess = int(temp)
    time = time + 1
    
if (guess == secret) and (time <= 3):
    print('correct')
else:
    print('chances is out')