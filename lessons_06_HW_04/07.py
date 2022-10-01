"""Game guess
 the number"""

from random import randint

number = randint(1,10)
a = int(input('Enter number: '))

while number != a:
    if a > number:
        print('Your number is greater than the given number')
    elif a < number:
        print('Your number is less than the given number')
    print('Please try again')
    a = int(input('Enter number: '))
else:
    print('You guessed!!!)))')

