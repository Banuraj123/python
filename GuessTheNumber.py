print('NAME:BANURAJ B K' ,'USN:1AY24AI015')
import random
number=random.randint(1,100)
guess=int(input("guess the number between 1 and 100:"))
if guess==number:
    print("you guessed it!!")
else:
    print(f"wrong! the number was {number}")
