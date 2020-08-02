temp = input('input a number')
guess = int(temp)

while (guess != 8) and (3 > 2):
    if guess > 8:
        print('lower')
    else:
        print('higher')
        
    temp = input('again')
    guess = int(temp)
    
print('correct')