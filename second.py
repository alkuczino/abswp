#Coin toss
import random
import sys

print('Zgadnij?')
result=random.randint(1,100)
while True:  
    guess=int(input())
    if guess > result:
        print('Mniej!!!')
    elif guess < result:
        print('Więcej!!!')
    else:
        print('Gratulacje!')
        sys.exit()
         